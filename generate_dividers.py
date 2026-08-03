width = 850
height = 30

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="line-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#020617" stop-opacity="0" />
      <stop offset="20%" stop-color="#38BDF8" stop-opacity="0.3" />
      <stop offset="50%" stop-color="#38BDF8" stop-opacity="1" />
      <stop offset="80%" stop-color="#38BDF8" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#020617" stop-opacity="0" />
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  <line x1="0" y1="15" x2="{width}" y2="15" stroke="url(#line-grad)" stroke-width="2" filter="url(#glow)"/>
</svg>'''

with open("divider.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Premium glowing divider generated.")
