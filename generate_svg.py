import math

width = 820
height = 280

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&amp;display=swap');
      
      @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to   {{ opacity: 1; }}
      }}
      @keyframes blink {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0; }}
      }}
      
      .bg {{
        fill: #0d1117;
      }}
      .pattern {{
        fill: #21262d;
      }}
      
      .name {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        font-size: 56px;
        font-weight: 700;
        letter-spacing: -2px;
        fill: #f0f6fc;
        opacity: 0;
        animation: fadeIn 0.8s ease-out forwards;
      }}
      .cursor {{
        fill: #8b949e;
        animation: blink 1s step-end infinite;
      }}
      
      .role {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 16px;
        font-weight: 500;
        fill: #8b949e;
        letter-spacing: 0px;
        opacity: 0;
        animation: fadeIn 0.8s ease-out 0.4s forwards;
      }}
      
      .divider-line {{
        stroke: #30363d;
        stroke-width: 1;
        opacity: 0;
        animation: fadeIn 0.8s ease-out 0.6s forwards;
      }}

      .tag-box {{
        fill: #161b22;
        stroke: #30363d;
        stroke-width: 1;
        rx: 4px;
        opacity: 0;
        animation: fadeIn 0.8s ease-out 0.8s forwards;
      }}
      
      .tag-text {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        fill: #c9d1d9;
        opacity: 0;
        animation: fadeIn 0.8s ease-out 0.8s forwards;
      }}
    </style>
    <pattern id="dot-grid" x="0" y="0" width="20" height="20" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="1.5" class="pattern" />
    </pattern>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" class="bg"/>
  <rect width="{width}" height="{height}" fill="url(#dot-grid)"/>

  <!-- Left Accent (Subtle GitHub Green) -->
  <line x1="50" y1="50" x2="50" y2="230" class="divider-line" style="stroke: #238636; stroke-width: 2;"/>

  <!-- Main Content -->
  <text x="80" y="120" class="name">Nithissh<tspan class="cursor">_</tspan></text>
  
  <text x="80" y="160" class="role">AI / ML Engineer &amp; Full-Stack Developer</text>
  
  <!-- Tags -->
  <!-- Tag 1 -->
  <rect x="80" y="190" width="85" height="28" class="tag-box" style="animation-delay: 0.8s;"/>
  <text x="92" y="209" class="tag-text" style="animation-delay: 0.8s;">Next.js</text>

  <!-- Tag 2 -->
  <rect x="175" y="190" width="75" height="28" class="tag-box" style="animation-delay: 0.9s;"/>
  <text x="187" y="209" class="tag-text" style="animation-delay: 0.9s;">Python</text>

  <!-- Tag 3 -->
  <rect x="260" y="190" width="85" height="28" class="tag-box" style="animation-delay: 1.0s;"/>
  <text x="272" y="209" class="tag-text" style="animation-delay: 1.0s;">PyTorch</text>

  <!-- Tag 4 -->
  <rect x="355" y="190" width="105" height="28" class="tag-box" style="animation-delay: 1.1s;"/>
  <text x="367" y="209" class="tag-text" style="animation-delay: 1.1s;">TypeScript</text>
</svg>'''

with open("animated_banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Done. Elegant advanced monochrome SVG generated.")
