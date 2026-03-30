#!/usr/bin/env node

import fs from "node:fs";
import path from "node:path";

const rootDir = path.resolve(path.dirname(new URL(import.meta.url).pathname), "..");
const errors = [];
const checks = [];

const skillRoots = ["skills", "skills-ko"];
const skillNames = ["start", "check", "fix", "guide"];

const expectedCiiCounts = {
  "admin.md": 127,
  "cloud.md": 19,
  "control-system.md": 46,
  "database.md": 26,
  "mobile.md": 4,
  "network.md": 38,
  "pc.md": 18,
  "physical.md": 18,
  "security-equip.md": 23,
  "unix.md": 67,
  "virtualization.md": 25,
  "web-service.md": 26,
  "webapp.md": 21,
  "windows.md": 64,
};

const expectedRobotCounts = {
  "cyber-resilience.md": 13,
  "iec62443.md": 50,
  "ssdf.md": 19,
  "supply-chain.md": 7,
  "wireless.md": 14,
};

const expectedStartReferenceCounts = {
  "references/cii/unix.md": 67,
  "references/cii/windows.md": 64,
  "references/cii/web-service.md": 26,
  "references/cii/security-equip.md": 23,
  "references/cii/network.md": 38,
  "references/cii/control-system.md": 46,
  "references/cii/pc.md": 18,
  "references/cii/database.md": 26,
  "references/cii/mobile.md": 4,
  "references/cii/webapp.md": 21,
  "references/cii/virtualization.md": 25,
  "references/cii/cloud.md": 19,
  "references/cii/admin.md": 127,
  "references/cii/physical.md": 18,
};

const expectedReadmeEnglishCounts = {
  "U-01~U-67": 67,
  "W-01~W-64": 64,
  "WEB-01~WEB-26": 26,
  "S-01~S-23": 23,
  "N-01~N-38": 38,
  "C-01~C-51": 46,
  "PC-01~PC-18": 18,
  "D-01~D-26": 26,
  "M-01~M-04": 4,
  "21 codes": 21,
  "HV-01~HV-25": 25,
  "CA-01~CA-19": 19,
};

const expectedReadmeKoreanCounts = {
  "U-01~U-67": 67,
  "W-01~W-64": 64,
  "WEB-01~WEB-26": 26,
  "S-01~S-23": 23,
  "N-01~N-38": 38,
  "C-01~C-51": 46,
  "PC-01~PC-18": 18,
  "D-01~D-26": 26,
  "M-01~M-04": 4,
  "21개 코드": 21,
  "HV-01~HV-25": 25,
  "CA-01~CA-19": 19,
};

function rel(filePath) {
  return path.relative(rootDir, filePath).replaceAll(path.sep, "/");
}

function read(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function assert(condition, message) {
  if (!condition) {
    errors.push(message);
  }
}

function check(name, fn) {
  checks.push(name);
  try {
    fn();
  } catch (error) {
    errors.push(`${name}: ${error instanceof Error ? error.message : String(error)}`);
  }
}

function listMarkdownFiles(dirPath) {
  const result = [];

  for (const entry of fs.readdirSync(dirPath, { withFileTypes: true })) {
    const entryPath = path.join(dirPath, entry.name);

    if (entry.isDirectory()) {
      result.push(...listMarkdownFiles(entryPath));
      continue;
    }

    if (entry.isFile() && entry.name.endsWith(".md")) {
      result.push(rel(entryPath));
    }
  }

  return result.sort();
}

function parseItemCountFromCell(cell) {
  const trimmed = cell.trim();

  if (/^(코드|Code|#|항목|Item|대상|Target)$/i.test(trimmed)) {
    return 0;
  }

  let match = trimmed.match(/^([A-Z]{1,5})-(\d+)\s*~\s*\1-(\d+)$/);
  if (match) {
    const start = Number(match[2]);
    const end = Number(match[3]);
    return end - start + 1;
  }

  match = trimmed.match(/^([A-Z]{1,5})-(\d+)$/);
  if (match) {
    return 1;
  }

  if (/^[A-Z]{2}$/.test(trimmed)) {
    return 1;
  }

  return 0;
}

function countReferenceItems(filePath) {
  return read(filePath)
    .split(/\r?\n/)
    .reduce((sum, line) => {
      const match = line.match(/^\|\s*([^|]+?)\s*\|/);
      return sum + (match ? parseItemCountFromCell(match[1]) : 0);
    }, 0);
}

function sectionBetween(content, startMarker, endMarker) {
  const start = content.indexOf(startMarker);
  if (start === -1) {
    return null;
  }

  const end = content.indexOf(endMarker, start + startMarker.length);
  if (end === -1) {
    return null;
  }

  return content.slice(start, end);
}

function parseStartReferenceTable(filePath) {
  const content = read(filePath);
  const rows = {};

  for (const line of content.split(/\r?\n/)) {
    const match = line.match(/^\|\s*[^|]+?\s*\|\s*`(references\/cii\/[^`]+)`\s*\|\s*(\d+)\s*\|$/);
    if (match) {
      rows[match[1]] = Number(match[2]);
    }
  }

  return rows;
}

function parseReadmeTechnicalTable(content, startMarker, endMarker) {
  const section = sectionBetween(content, startMarker, endMarker);
  if (!section) {
    return null;
  }

  const rows = {};

  for (const line of section.split(/\r?\n/)) {
    const match = line.match(/^\|\s*[^|]+?\s*\|\s*([^|]+?)\s*\|\s*(\d+)\s*\|$/);
    if (match) {
      rows[match[1].trim()] = Number(match[2]);
    }
  }

  return rows;
}

function assertObjectEqual(actual, expected, name) {
  const actualJson = JSON.stringify(actual, Object.keys(actual).sort());
  const expectedJson = JSON.stringify(expected, Object.keys(expected).sort());
  assert(actualJson === expectedJson, `${name} mismatch.\nactual: ${actualJson}\nexpected: ${expectedJson}`);
}

function assertIncludes(filePath, pattern, description) {
  const content = read(filePath);
  const ok = pattern instanceof RegExp ? pattern.test(content) : content.includes(pattern);
  assert(ok, `${rel(filePath)} is missing ${description}`);
}

check("reference-tree-parity", () => {
  for (const skillRoot of skillRoots) {
    const baseDir = path.join(rootDir, skillRoot, "start", "references");
    const expectedFiles = listMarkdownFiles(baseDir).map((file) => file.replace(`${skillRoot}/start/`, ""));

    for (const skillName of skillNames.slice(1)) {
      const dirPath = path.join(rootDir, skillRoot, skillName, "references");
      const actualFiles = listMarkdownFiles(dirPath).map((file) => file.replace(`${skillRoot}/${skillName}/`, ""));
      assertObjectEqual(actualFiles, expectedFiles, `${skillRoot}/${skillName}/references file list`);
    }
  }
});

check("reference-content-parity", () => {
  for (const skillRoot of skillRoots) {
    const baseDir = path.join(rootDir, skillRoot, "start", "references");
    const relativeFiles = listMarkdownFiles(baseDir).map((file) => file.replace(`${skillRoot}/start/`, ""));

    for (const relativeFile of relativeFiles) {
      const baseline = read(path.join(rootDir, skillRoot, "start", relativeFile));

      for (const skillName of skillNames.slice(1)) {
        const candidatePath = path.join(rootDir, skillRoot, skillName, relativeFile);
        const candidate = read(candidatePath);
        assert(
          candidate === baseline,
          `${rel(candidatePath)} diverged from ${skillRoot}/start/${relativeFile}`,
        );
      }
    }
  }
});

check("cii-reference-counts", () => {
  const ciiDir = path.join(rootDir, "skills", "start", "references", "cii");

  for (const [fileName, expectedCount] of Object.entries(expectedCiiCounts)) {
    const filePath = path.join(ciiDir, fileName);
    const actualCount = countReferenceItems(filePath);
    assert(actualCount === expectedCount, `${rel(filePath)} expected ${expectedCount} items, found ${actualCount}`);
  }
});

check("robot-reference-counts", () => {
  const robotDir = path.join(rootDir, "skills", "start", "references", "robot-security");
  let total = 0;

  for (const [fileName, expectedCount] of Object.entries(expectedRobotCounts)) {
    const filePath = path.join(robotDir, fileName);
    const actualCount = countReferenceItems(filePath);
    total += actualCount;
    assert(actualCount === expectedCount, `${rel(filePath)} expected ${expectedCount} items, found ${actualCount}`);
  }

  assert(total === 103, `Robot Security total expected 103 items, found ${total}`);
});

check("start-skill-count-tables", () => {
  const englishStart = parseStartReferenceTable(path.join(rootDir, "skills", "start", "SKILL.md"));
  const koreanStart = parseStartReferenceTable(path.join(rootDir, "skills-ko", "start", "SKILL.md"));

  assertObjectEqual(englishStart, expectedStartReferenceCounts, "skills/start/SKILL.md reference table");
  assertObjectEqual(koreanStart, expectedStartReferenceCounts, "skills-ko/start/SKILL.md reference table");
});

check("readme-count-tables", () => {
  const content = read(path.join(rootDir, "README.md"));
  const englishTable = parseReadmeTechnicalTable(content, "**Technical Assessment**", "**Administrative Assessment**");
  const koreanTable = parseReadmeTechnicalTable(content, "**기술적 취약점 평가**", "**관리적 취약점 평가**");

  assert(englishTable !== null, "README.md English technical assessment table was not found");
  assert(koreanTable !== null, "README.md Korean technical assessment table was not found");

  if (englishTable) {
    assertObjectEqual(englishTable, expectedReadmeEnglishCounts, "README.md English CII count table");
  }

  if (koreanTable) {
    assertObjectEqual(koreanTable, expectedReadmeKoreanCounts, "README.md Korean CII count table");
  }
});

check("router-robot-branch-coverage", () => {
  assertIncludes(path.join(rootDir, "skills", "start", "SKILL.md"), /## Robot Security Branch/, "an English Robot Security branch section");
  assertIncludes(path.join(rootDir, "skills", "check", "SKILL.md"), /## Robot Security Branch/, "an English Robot Security branch section");
  assertIncludes(path.join(rootDir, "skills", "fix", "SKILL.md"), /## Robot Security Branch/, "an English Robot Security branch section");
  assertIncludes(path.join(rootDir, "skills", "guide", "SKILL.md"), /## Robot Security Branch/, "an English Robot Security branch section");

  assertIncludes(path.join(rootDir, "skills-ko", "start", "SKILL.md"), /## 로봇 보안 분기 시/, "a Korean robot branch section");
  assertIncludes(path.join(rootDir, "skills-ko", "check", "SKILL.md"), /## 로봇 보안 분기 시/, "a Korean robot branch section");
  assertIncludes(path.join(rootDir, "skills-ko", "fix", "SKILL.md"), /## 로봇 보안 분기 시/, "a Korean robot branch section");
  assertIncludes(path.join(rootDir, "skills-ko", "guide", "SKILL.md"), /## 로봇 보안 분기 시/, "a Korean robot branch section");
});

check("metadata-mentions-robot-security", () => {
  assertIncludes(path.join(rootDir, ".claude-plugin", "marketplace.json"), /Robot Security|로봇 보안/, "Robot Security metadata");
  assertIncludes(path.join(rootDir, "README.md"), /Robot Security/, "Robot Security in the English README");
  assertIncludes(path.join(rootDir, "README.md"), /로봇 보안/, "robot security in the Korean README");
});

if (errors.length > 0) {
  console.error(`Validation failed with ${errors.length} issue(s):`);
  for (const error of errors) {
    console.error(`- ${error}`);
  }
  process.exit(1);
}

console.log(`Validated ${checks.length} content checks successfully.`);
