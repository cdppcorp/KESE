#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Clean up extracted PDF images: remove duplicates, decorative backgrounds, tiny fragments."""

import os
import hashlib
import re
import sys

def md5(filepath):
    with open(filepath, 'rb') as f:
        return hashlib.md5(f.read()).hexdigest()

def cleanup_images(ref_dir):
    images_dir = os.path.join(ref_dir, "images")
    full_md_path = os.path.join(ref_dir, "full.md")

    if not os.path.exists(images_dir):
        print(f"No images dir: {images_dir}")
        return

    # 1. Scan all images
    all_images = sorted([f for f in os.listdir(images_dir) if f.endswith('.png')])
    print(f"Total images before cleanup: {len(all_images)}")

    hash_map = {}  # hash -> first file
    to_delete = set()
    reasons = {}

    for img in all_images:
        img_path = os.path.join(images_dir, img)
        size = os.path.getsize(img_path)
        h = md5(img_path)

        # Rule 1: 0 byte files
        if size == 0:
            to_delete.add(img)
            reasons[img] = "0 bytes"
            continue

        # Rule 2: Under 5KB - too small to be meaningful (icons, dots, fragments)
        if size < 5120:
            to_delete.add(img)
            reasons[img] = f"too small ({size} bytes)"
            continue

        # Rule 3: Duplicates - keep first, delete rest
        if h in hash_map:
            to_delete.add(img)
            reasons[img] = f"duplicate of {hash_map[h]}"
            continue

        hash_map[h] = img

    # Rule 4: Identify decorative backgrounds (appear 5+ times = page decoration)
    hash_counts = {}
    for img in all_images:
        if img in to_delete:
            continue
        img_path = os.path.join(images_dir, img)
        h = md5(img_path)
        hash_counts[h] = hash_counts.get(h, 0) + 1

    # Any remaining hash that appeared many times in the original set is decorative
    # Count from ALL images (before dedup) to catch patterns
    all_hashes = {}
    for img in all_images:
        img_path = os.path.join(images_dir, img)
        if os.path.getsize(img_path) > 0:
            h = md5(img_path)
            if h not in all_hashes:
                all_hashes[h] = []
            all_hashes[h].append(img)

    decorative_hashes = set()
    for h, files in all_hashes.items():
        if len(files) >= 5:  # appears 5+ times = page decoration pattern
            decorative_hashes.add(h)
            for f in files:
                if f not in to_delete:
                    to_delete.add(f)
                    reasons[f] = f"decorative background (appeared {len(files)}x)"

    # Summary
    print(f"\nImages to delete: {len(to_delete)}")
    reason_counts = {}
    for r in reasons.values():
        key = r.split('(')[0].strip() if '(' in r else r.split(' of ')[0].strip() if ' of ' in r else r
        reason_counts[key] = reason_counts.get(key, 0) + 1
    for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
        print(f"  - {reason}: {count}")

    # Delete files
    for img in to_delete:
        img_path = os.path.join(images_dir, img)
        if os.path.exists(img_path):
            os.remove(img_path)

    remaining = [f for f in os.listdir(images_dir) if f.endswith('.png')]
    print(f"\nImages remaining: {len(remaining)}")

    # Update full.md - remove references to deleted images
    if os.path.exists(full_md_path):
        with open(full_md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_len = len(content)
        lines = content.split('\n')
        cleaned_lines = []
        removed_refs = 0

        for line in lines:
            # Check if line references a deleted image
            match = re.search(r'!\[.*?\]\(images/(.+?)\)', line)
            if match and match.group(1) in to_delete:
                removed_refs += 1
                continue  # skip this line
            cleaned_lines.append(line)

        # Remove excessive blank lines (3+ consecutive -> 2)
        content = '\n'.join(cleaned_lines)
        content = re.sub(r'\n{4,}', '\n\n\n', content)

        with open(full_md_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Removed {removed_refs} image references from full.md")
        print(f"Markdown size: {original_len:,} -> {len(content):,} chars")

    # Update conversion log
    log_path = os.path.join(ref_dir, "conversion-log.md")
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding='utf-8') as f:
            log = f.read()
        log += f"\n## Cleanup ({__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')})\n\n"
        log += f"- Deleted: {len(to_delete)} images\n"
        log += f"- Remaining: {len(remaining)} images\n"
        for reason, count in sorted(reason_counts.items(), key=lambda x: -x[1]):
            log += f"  - {reason}: {count}\n"
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(log)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cleanup_images.py <ref_dir>")
        sys.exit(1)
    cleanup_images(sys.argv[1])
