---
title: "GitHub for Pilots and Builders: A Complete Beginner's Guide"
date: 2026-04-11T08:00:00-06:00
description: "Never used GitHub before? You don't need to be a software developer to use it. This guide explains what GitHub is, why AeroCommons uses it, and how to set up a project repository — using only a web browser."
tags: ["github", "community", "education", "getting-started"]
author: "AeroCommons"
article_type: "guide"
draft: false
---

AeroCommons requires that projects have a public GitHub repository. If you've never heard of GitHub — or you've heard of it but always assumed it was for software people — this guide is for you.

You do not need to write code. You do not need to install anything. Everything in this guide can be done in a web browser.

---

## What Is GitHub?

GitHub is a website where you store, organize, and track files — and where other people can find them, follow along, and contribute.

It was designed by software developers, which is why it can feel unfamiliar if your world is airplanes rather than code. But the core idea is simple and genuinely useful for aviation projects:

- Every file you upload is stored permanently
- Every change to every file is recorded — what changed, when, and a note about why
- Anyone in the world can read your files and download them for free
- People can ask questions, flag problems, and suggest changes — and all of that conversation stays attached to the specific file or topic it's about

Think of it as a combination of three things:

1. **A shared filing cabinet** — your PDFs, drawings, spreadsheets, photos, and documents all in one place that anyone can access
2. **A maintenance logbook** — a complete history of every change, who made it, and why, going back to day one
3. **An open forum** — where readers can ask questions and you can respond, with the whole conversation preserved

If you've ever lost track of which version of a drawing was the latest one, or had a file stuck on your laptop that no one else could see, GitHub solves both of those problems.

---

## Why Does AeroCommons Use It?

The short answer: because open-source aviation only works if the work is actually open.

Sending files by email creates private conversations that disappear. Google Drive links break. Facebook posts get buried. PDFs on a personal website don't have a comment thread, a change history, or a way for someone to propose a fix.

GitHub gives a project:

- A permanent, stable home for every file
- A public record of all design decisions and changes
- A community space where experienced builders can leave specific feedback on specific documents
- A way for other builders to take your work and adapt it for their own projects

This is how open-source software development works, and it turns out the same workflow maps well to aircraft design. AeroCommons itself is built on GitHub — every article, drawing, and design file for every hosted project lives there.

---

## Step 1: Create a Free GitHub Account

Go to **[github.com](https://github.com)** and click **Sign up**.

You'll need:
- An email address
- A username (this becomes part of your project's URL — something like `github.com/yourusername/your-project`)
- A password

GitHub is free for public repositories. You never need to pay for anything to use AeroCommons.

**Tip on username:** Pick something you'd be comfortable with on a business card. Your GitHub profile represents your project publicly. `jsmith-aviation` is better than `jsmith1974xp`.

---

## Step 2: Create Your Project Repository

A **repository** (usually called a "repo") is the container that holds all of your project's files. Think of it as the top-level folder for your project.

1. After signing in, click the **+** icon in the top-right corner and select **New repository**
2. Give it a name — use hyphens instead of spaces (e.g., `smith-long-ez-restoration` or `rv-14-fuel-system`)
3. Write a short description — one sentence about what the project is
4. Set it to **Public** (required for AeroCommons submission — your work needs to be readable without a login)
5. Check **Add a README file** — this creates the main description page for your project
6. Under **Choose a license**, select **CC0** or **CC BY 4.0** for design files, or leave it blank if you're not sure yet
7. Click **Create repository**

That's it. Your project now has a public home on the internet.

---

## Step 3: Set Up a Basic Folder Structure

You don't need a complex folder structure to submit a project. But a consistent layout makes your repo easier to navigate for anyone who finds it.

Here's a simple starting point for a GA project:

```
your-project-name/
├── README.md              ← project description (auto-created in Step 2)
├── docs/                  ← PDFs, design reports, analysis write-ups
│   ├── DESIGN-OVERVIEW.pdf
│   └── WEIGHT-BUDGET.xlsx
├── cad/                   ← CAD files, drawings, DXF, STEP, STL
│   └── wing-rib-template.dxf
└── photos/                ← build photos, reference images
    └── fuselage-frame-2026-03-15.jpg
```

To create a folder on GitHub using only the browser:

1. In your repository, click **Add file → Create new file**
2. In the filename box, type `docs/` — GitHub will create the folder automatically when you include a `/`
3. Add a placeholder filename like `docs/.gitkeep` (an empty file to hold the folder)
4. Scroll down and click **Commit new file**

Repeat for any other folders you want.

---

## Step 4: Upload Your Files

You don't need any special software to add files to your repository.

1. Navigate to the folder you want to upload into (e.g., click on `docs/`)
2. Click **Add file → Upload files**
3. Drag and drop files from your computer, or click **choose your files** to browse
4. Under **Commit changes**, add a short note describing what you're uploading (e.g., "Add initial weight budget spreadsheet")
5. Click **Commit changes**

That's it. The file is now online, publicly accessible, and version-tracked.

**On commit messages:** Get in the habit of writing useful notes. "Add file" tells nobody anything. "Add wing rib template — 0.032 2024-T3, based on Bingelis Chapter 4" is still just one line but tells a future reader — including future you — exactly what they need to know.

---

## Step 5: Write Your README

The README is the first thing anyone sees when they visit your repository. GitHub displays it automatically on the front page of your repo.

You don't need to write code to edit it. Click on `README.md` in your file list, then click the **pencil icon** (Edit) in the top-right corner of the file view.

A useful README for an aviation project answers these questions:

1. **What is this project?** One or two sentences.
2. **What stage is it at?** (Concept, design, under construction, flying, restoration, etc.)
3. **What's in the repository?** A short list of what files exist and what they are.
4. **How can someone follow along or get involved?**
5. **Any important disclaimers** — especially the standard aviation one: *This repository is for informational and educational purposes. Nothing here constitutes airworthiness approval. Build and fly at your own judgment and risk.*

When you're done editing, scroll down and click **Commit changes**.

---

## How to Participate Without Writing Code

A lot of the value in GitHub happens in two places that don't involve files at all.

### Discussions

The **Discussions** tab on a repository is a community forum attached directly to the project. You can:

- Ask questions about design decisions
- Share relevant experience from your own builds or flying
- Follow conversations on specific topics
- Propose ideas or flag concerns

Questions asked in Discussions are indexed and searchable. A question you ask today may help a builder three years from now find the same information.

### Issues

The **Issues** tab is for specific, trackable problems. If you find something in a document that looks wrong — a calculation that doesn't add up, a specification that conflicts with another document, a drawing that's missing a dimension — open an Issue.

Issues create a tracked record. They don't disappear into an email thread. The project maintainer can address them directly and close the issue when it's resolved, leaving a permanent record of what the problem was and how it was fixed.

You don't need to know the answer to open an issue. You just need to be specific about what you observed.

---

## Submitting Your Project to AeroCommons

Once your repository is set up and has at least a README and some documentation, you're ready to submit.

See [/submit/](/submit/) for the current requirements and submission process.

The short version: email [contact@aerocommons.org](mailto:contact@aerocommons.org) with your GitHub repository link and a brief description. We'll review it and respond within two weeks.

If you have questions about whether your project is a good fit, or if you're not sure your repository is ready, just email us — we'd rather answer a question upfront than have you spend time on a submission that needs work.

---

## GitHub's Own Resources

GitHub maintains good documentation aimed at complete beginners:

- [Getting started with GitHub](https://docs.github.com/en/get-started) — official documentation
- [GitHub Skills](https://skills.github.com/) — interactive beginner courses (free, browser-based)
- [GitHub Discussions documentation](https://docs.github.com/en/discussions) — how Discussions work

None of these require you to install anything or understand software development. The GitHub Skills courses in particular are well-designed for someone who's never touched version control before.

---

*AeroCommons is a non-profit organization. We don't charge for hosting or take ownership of submitted projects. Your work remains yours under whatever license you choose.*
