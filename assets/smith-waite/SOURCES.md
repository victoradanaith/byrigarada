# Smith Waite tarot images: sources

All 78 images come from Wikimedia Commons, category "Rider-Waite tarot deck (Roses & Lilies)".
Each is a scan of an original 1909 "Roses & Lilies" printing of the Rider–Waite–Smith deck (art by Pamela Colman Smith, 1909), scanned by Saskia Jansen from her collection, and marked **Public domain** on Commons.

`sources.json` lists every card's Commons file page, licence, pixel size and SHA-1. Each downloaded file was checked against that SHA-1 before processing.

**Processing (2026-11-18, after reviewer feedback that the cards looked too yellow and the corners were cut unevenly):** each scan was cropped to its printed black frame (removing the scan background and worn, rounded paper corners), its colour was neutralised by mapping each channel's 99th percentile to the same light value (this removes the yellow cast of aged paper; the printed colours are otherwise unchanged), and it was resized to 588x1048 and placed on an even 16 px light border (620x1080). The SHA-1 values in `sources.json` are for the original Commons files, not the processed ones. The script is `tools/sw_fix.py`.

These are not U.S. Games Systems' Smith-Waite Centennial scans. That edition reproduces the same 1909 colouring, but its restoration and scans are U.S. Games' own work, so this page uses the public-domain 1909 scans instead. Colours can differ slightly from a printed Centennial deck because of paper ageing and scanning.
