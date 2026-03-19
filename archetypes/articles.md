---
title: "{{ replace .Name "-" " " | title }}"
date: {{ .Date }}
description: ""
tags: []
author: "AeroCommons Design Board"
session: ""
summary: ""
draft: false
---

<!-- 
  AEROCOMMONS ARTICLE TEMPLATE
  ─────────────────────────────
  title:       Full title of the post
  date:        ISO 8601 — YYYY-MM-DDTHH:MM:SS-06:00
  description: One sentence shown in article cards and meta tags
  tags:        Array of lowercase tags e.g. ["board-meeting", "propulsion", "structures"]
  author:      Who or what produced this (e.g. "AeroCommons Design Board")
  session:     Optional — board session ID if applicable (e.g. "BOARD-004")
  summary:     Optional — override for the article card excerpt
  draft:       Set to true to publish to repo without displaying on site
-->

Body content begins here. Markdown is fully supported.
