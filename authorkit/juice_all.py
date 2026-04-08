"""
AI 기본법 PDF -> Markdown Juice 스크립트
10개 PDF를 마크다운으로 변환 (텍스트 + 이미지 추출)
"""
import fitz
import os
import re
import sys
from pathlib import Path

BASE = Path("C:/Users/admin/PycharmProjects/PawnERP/Skills/KESE/authorkit/new pdf/ai기본법")
OUT = Path("C:/Users/admin/PycharmProjects/PawnERP/Skills/KESE/authorkit/juiced/ai기본법")

FILES = [
    ("01_인공지능기본법_법률원문", "인공지능_발전과_신뢰_기반_조성_등에_관한_기본법(법률)(제21311호)(20260122)[1].pdf"),
    ("02_인공지능기본법_시행령", "인공지능_발전과_신뢰_기반_조성_등에_관한_기본법_시행령_제정안[1].pdf"),
    ("03_투명성확보_가이드라인", "1._260126_투명성_확보_가이드라인_최종본(1.22._공개용)_수정본.pdf"),
    ("04_안전성확보_가이드라인", "2._260122_인공지능_안전성_확보_가이드라인[1].pdf"),
    ("05_최첨단AI_안전성확보_가이드라인", "260122_최첨단_인공지능_안전성_확보_가이드라인 (1).pdf"),
    ("06_고영향AI_판단_가이드라인_v4", "3._260213_고영향_인공지능_판단_가이드라인_최종_v.4.pdf"),
    ("07_고영향AI_사업자책무_가이드라인", "4._260122_고영향_인공지능_사업자_책무_가이드라인-1[1].pdf"),
    ("08_인공지능_영향평가_가이드라인", "5._260122_인공지능_영향평가_가이드라인[1].pdf"),
    ("09_국내대리인_지정절차_안내", "260122_AI기본법상_국내대리인_지정_절차_안내[1].pdf"),
    ("10_지원데스크_사례집", "인공지능기본법_지원데스크_사례집.pdf"),
]


def clean_text(text: str) -> str:
    """노이즈 제거: 머리글/바닥글, 페이지 번호, 과도한 공백"""
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        stripped = line.strip()
        # 빈 줄은 하나만 유지
        if not stripped:
            if cleaned and cleaned[-1] == "":
                continue
            cleaned.append("")
            continue
        # 페이지 번호만 있는 줄 제거
        if re.match(r'^[-–—]?\s*\d{1,3}\s*[-–—]?$', stripped):
            continue
        # 반복되는 머리글/바닥글 패턴 제거
        if re.match(r'^(인공지능\s*(기본법|발전)|제\d+조|부\s*칙)\s*$', stripped) and len(stripped) < 15:
            pass  # 이건 실제 내용일 수 있으므로 유지
        cleaned.append(stripped)
    return "\n".join(cleaned)


def detect_headings(text: str) -> str:
    """텍스트에서 제목/소제목 패턴 감지하여 마크다운 헤딩으로 변환"""
    lines = text.split("\n")
    result = []
    for line in lines:
        stripped = line.strip()
        # 장/편/절 패턴
        if re.match(r'^제\s*\d+\s*장\b', stripped):
            result.append(f"\n## {stripped}\n")
        elif re.match(r'^제\s*\d+\s*편\b', stripped):
            result.append(f"\n## {stripped}\n")
        elif re.match(r'^제\s*\d+\s*절\b', stripped):
            result.append(f"\n### {stripped}\n")
        elif re.match(r'^제\s*\d+\s*조(\s*[\(（])', stripped):
            result.append(f"\n#### {stripped}\n")
        # 숫자. 제목 패턴 (1. 개요, 2. 목적 등)
        elif re.match(r'^\d+\.\s+\S', stripped) and len(stripped) < 80:
            result.append(f"\n### {stripped}\n")
        # I, II, III 등 로마숫자 패턴
        elif re.match(r'^(I{1,3}|IV|V|VI{0,3}|VII|VIII|IX|X)\.\s+\S', stripped):
            result.append(f"\n## {stripped}\n")
        # 가. 나. 다. 패턴
        elif re.match(r'^[가-힣]\.\s+', stripped) and len(stripped) < 60:
            result.append(f"\n**{stripped}**\n")
        else:
            result.append(stripped)
    return "\n".join(result)


def extract_pdf(name: str, filename: str, skip_large_images: bool = False):
    """PDF에서 텍스트와 이미지를 추출하여 마크다운 생성"""
    fpath = BASE / filename
    if not fpath.exists():
        print(f"  [SKIP] 파일 없음: {filename}")
        return

    doc = fitz.open(str(fpath))
    total_pages = len(doc)
    print(f"  처리중: {name} ({total_pages}p)")

    # 이미지 디렉토리
    img_dir = OUT / name / "images"
    img_dir.mkdir(parents=True, exist_ok=True)

    md_lines = []
    md_lines.append(f"# {name.split('_', 1)[1].replace('_', ' ')}\n")
    md_lines.append(f"> 원본: `{filename}`  ")
    md_lines.append(f"> 페이지: {total_pages}p\n")
    md_lines.append("---\n")

    img_count = 0
    for page_num in range(total_pages):
        page = doc[page_num]

        # 텍스트 추출
        text = page.get_text("text")
        text = clean_text(text)
        text = detect_headings(text)

        if text.strip():
            md_lines.append(text)

        # 이미지 추출
        if skip_large_images and page_num > 0:
            # 대용량 파일은 처음 몇 페이지만 이미지 추출
            images = page.get_images() if page_num < 30 else []
        else:
            images = page.get_images()

        for img_idx, img in enumerate(images):
            try:
                xref = img[0]
                pix = fitz.Pixmap(doc, xref)

                # 너무 작은 이미지 건너뛰기 (아이콘, 장식 등)
                if pix.width < 50 or pix.height < 50:
                    pix = None
                    continue

                # CMYK -> RGB
                if pix.n >= 5:
                    pix = fitz.Pixmap(fitz.csRGB, pix)

                img_fname = f"p{page_num+1:03d}_img{img_idx}.png"
                img_path = img_dir / img_fname
                pix.save(str(img_path))
                img_count += 1

                # 마크다운에 이미지 참조 삽입
                md_lines.append(f"\n![그림 - p{page_num+1}](images/{img_fname})\n")
                pix = None
            except Exception as e:
                print(f"    [WARN] 이미지 추출 실패 p{page_num+1}: {e}")

        # 페이지 구분 (매 10페이지마다)
        if (page_num + 1) % 10 == 0:
            sys.stdout.write(f"\r    {page_num+1}/{total_pages}p 완료...")
            sys.stdout.flush()

    doc.close()

    # 마크다운 파일 저장
    md_path = OUT / name / f"{name}.md"
    md_path.parent.mkdir(parents=True, exist_ok=True)
    with open(str(md_path), "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))

    print(f"\r    완료: {total_pages}p, 이미지 {img_count}개 -> {md_path.name}")
    return str(md_path)


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    # 특정 파일만 처리하려면 인자로 번호 전달 (예: python juice_all.py 06)
    target = sys.argv[1] if len(sys.argv) > 1 else None

    results = []
    for name, filename in FILES:
        num = name[:2]
        if target and num != target:
            continue

        # 06번(86MB)은 이미지 추출 제한
        skip_large = (num == "06")
        result = extract_pdf(name, filename, skip_large_images=skip_large)
        if result:
            results.append(result)

    print(f"\n총 {len(results)}개 파일 juice 완료")
    for r in results:
        print(f"  -> {r}")


if __name__ == "__main__":
    main()
