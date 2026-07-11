import math

width = 820
height = 280

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @keyframes slideUp {{
        from {{ opacity: 0; transform: translateY(18px); }}
        to   {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes expandLine {{
        from {{ stroke-dashoffset: 300; }}
        to   {{ stroke-dashoffset: 0; }}
      }}
      @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to   {{ opacity: 1; }}
      }}
      .name {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        font-size: 52px;
        font-weight: 700;
        letter-spacing: -1.5px;
        fill: #f1f5f9;
        animation: slideUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.1s both;
      }}
      .role {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        font-size: 16px;
        font-weight: 400;
        fill: #64748b;
        letter-spacing: 0.5px;
        animation: slideUp 0.7s cubic-bezier(0.16, 1, 0.3, 1) 0.3s both;
      }}
      .dot {{
        fill: #38bdf8;
        animation: fadeIn 0.4s ease 0.8s both;
      }}
      .accent-line {{
        stroke: #38bdf8;
        stroke-width: 2;
        stroke-dasharray: 300;
        stroke-dashoffset: 300;
        animation: expandLine 1s cubic-bezier(0.16, 1, 0.3, 1) 0.5s forwards;
      }}
      .tag {{
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
        font-size: 12px;
        fill: #475569;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        animation: fadeIn 0.6s ease 0.9s both;
      }}
      .divider {{
        stroke: #1e293b;
        stroke-width: 1;
        animation: fadeIn 0.6s ease 0.4s both;
      }}
    </style>
  </defs>

  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#0d1117"/>

  <!-- Left vertical rule -->
  <line x1="52" y1="60" x2="52" y2="220" class="divider"/>

  <!-- Accent line (horizontal, under name) -->
  <line x1="72" y1="158" x2="372" y2="158" class="accent-line"/>

  <!-- Name -->
  <text x="72" y="148" class="name">Nithissh<tspan class="dot">.</tspan></text>

  <!-- Role line -->
  <text x="74" y="185" class="role">AI / ML Engineer  ·  Full-Stack Developer</text>

  <!-- Tags row -->
  <text x="74" y="218" class="tag">Next.js  ·  Python  ·  PyTorch  ·  TypeScript</text>

</svg>'''

with open("animated_banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Done. Minimal professional SVG generated.")
