ShiftLeft brand asset pack — 2025-10-23

Colors:
- Pink: #f00041
- Navy: #00283c

Install:
1) Copy everything to: manuals_src/static/img/brand/
2) In manuals_src/docusaurus.config.ts set favicon: 'img/brand/favicon-32.png'
3) Import 'src/css/custom.css' and paste custom-colors.css contents there.
4) (Optional) Add site.webmanifest to static root and reference it in Head:
   <link rel="manifest" href="/img/brand/site.webmanifest">

Files:
- favicon-16/32/48/64/180/192/256/384/512.png
- favicon.ico (multi-res)
- site.webmanifest
- Shiftleft_LogoHorizontal_V*.png, Shiftleft_LogoVertical_V1.png
- icon.png (original mark)
- custom-colors.css (snippet)
- docusaurus-config-snippet.ts
