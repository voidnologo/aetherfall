const fs = require('fs');
const path = require('path');
const MarkdownIt = require('markdown-it');

const md = new MarkdownIt({
  html: false,
  linkify: false,
  typographer: false,
  breaks: false,
});

function renderChapter(raw) {
  const cleaned = raw
    .replace(/^#\s+Chapter\s+\d+\s*$/m, '')
    .trim();
  return md.render(cleaned);
}

function countWords(text) {
  return text.trim().split(/\s+/).length;
}

function loadChapters(storyDir, povOrder) {
  const chapters = [];
  for (let i = 1; i <= povOrder.length; i++) {
    const file = path.join(storyDir, `ch${String(i).padStart(2, '0')}.md`);
    if (!fs.existsSync(file)) continue;
    const raw = fs.readFileSync(file, 'utf8');
    chapters.push({
      num: i,
      numDisplay: String(i).padStart(2, '0'),
      pov: povOrder[i - 1],
      words: countWords(raw),
      html: renderChapter(raw),
    });
  }
  return chapters;
}

function buildStory(config) {
  const storyDir = path.join(__dirname, '..', '..', 'fiction', 'stories', config.dir);
  const chapters = loadChapters(storyDir, config.povOrder);
  const totalWords = chapters.reduce((a, c) => a + c.words, 0);
  const readMinutes = Math.round(totalWords / 240);
  return {
    slug: config.slug,
    number: config.number,
    numberDisplay: String(config.number).padStart(2, '0'),
    wordsDisplay: totalWords.toLocaleString('en-US'),
    title: config.title,
    subtitle: config.subtitle,
    blurb: config.blurb,
    tagline: config.tagline,
    location: config.location,
    tone: config.tone,
    totalWords,
    readMinutes,
    chapters,
  };
}

const STORY_02 = {
  dir: 'story-02',
  slug: 'what-the-mill-remembered',
  number: 2,
  title: 'What the Mill Remembered',
  subtitle: 'A Tale of the Ash & Veil Society',
  blurb: 'A rushed patron job sends a young Society into the Wilds northeast of Ashwick, hunting an artifact rumored inside a pre-Tear mill whose interior has been remade into something the builders would not recognize — and they are not the only ones looking.',
  tagline: 'A short story of the Ash & Veil Society',
  location: 'Ashwick &mdash; and the Wilds beyond',
  tone: 'Propulsive, wonder-threaded, dark at the edges',
  povOrder: ['Mira', 'Kael', 'Sera', 'Aldric', 'Mira', 'Sera', 'Kael', 'Aldric', 'Kael', 'Mira'],
};

const STORY_03 = {
  dir: 'story-03',
  slug: 'the-lamplighters-price',
  number: 3,
  title: "The Lamplighter's Price",
  subtitle: 'A Tale of the Ash & Veil Society',
  blurb: "A Syndicate fixer walks into the Society's favourite tavern carrying blackmail, a job, and a knowing smile. Beneath a decommissioned Galvanic foundry the drainage tunnels have been changing — the same agency that remade the mill in the Wilds is at work here, in territory where Aetheric activity should be impossible.",
  tagline: 'A short story of the Ash & Veil Society',
  location: 'Ashwick &mdash; beneath the Factory Quarter',
  tone: 'Claustrophobic, noir-inflected, morally compromised',
  povOrder: ['Kael', 'Mira', 'Sera', 'Aldric', 'Kael', 'Sera', 'Kael', 'Aldric'],
};

module.exports = function () {
  const stories = [STORY_03, STORY_02].map(buildStory);
  const storiesBySlug = Object.fromEntries(stories.map(s => [s.slug, s]));
  return { stories, storiesBySlug };
};
