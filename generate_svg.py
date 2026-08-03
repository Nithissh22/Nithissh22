import math
import random

width = 850
height = 320

# Generate some nodes for a neural network background
random.seed(42) # fixed seed for consistent rendering
num_nodes = 40
nodes = []
for i in range(num_nodes):
    nodes.append({
        'x': random.randint(0, width),
        'y': random.randint(0, height),
        'r': random.uniform(1.5, 3.0),
        'delay': random.uniform(0, 4)
    })

# Connect nodes that are close to each other
lines = []
for i in range(num_nodes):
    for j in range(i+1, num_nodes):
        dx = nodes[i]['x'] - nodes[j]['x']
        dy = nodes[i]['y'] - nodes[j]['y']
        dist = math.sqrt(dx*dx + dy*dy)
        if dist < 120:
            lines.append({
                'x1': nodes[i]['x'], 'y1': nodes[i]['y'],
                'x2': nodes[j]['x'], 'y2': nodes[j]['y'],
                'opacity': 1.0 - (dist / 120.0)
            })

lines_svg = ""
for line in lines:
    lines_svg += f'<line x1="{line["x1"]}" y1="{line["y1"]}" x2="{line["x2"]}" y2="{line["y2"]}" stroke="rgba(56, 189, 248, {line["opacity"] * 0.4})" stroke-width="0.8" class="net-line"/>\n'

nodes_svg = ""
for node in nodes:
    nodes_svg += f'<circle cx="{node["x"]}" cy="{node["y"]}" r="{node["r"]}" fill="#38BDF8" opacity="0.7" style="animation: pulse 4s infinite {node["delay"]}s ease-in-out;" />\n'


svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&amp;display=swap');
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&amp;display=swap');
      
      @keyframes float {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-10px); }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 0.2; transform: scale(1); }}
        50% {{ opacity: 0.9; transform: scale(1.6); filter: drop-shadow(0 0 4px #38BDF8); }}
      }}
      @keyframes dash {{
        to {{ stroke-dashoffset: 0; }}
      }}
      @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
      }}
      @keyframes glow {{
        0%, 100% {{ filter: drop-shadow(0 0 15px rgba(56, 189, 248, 0.4)); }}
        50% {{ filter: drop-shadow(0 0 25px rgba(56, 189, 248, 0.8)); }}
      }}
      
      .bg-gradient {{
        fill: url(#bg-grad);
      }}
      
      .net-line {{
        stroke-dasharray: 200;
        stroke-dashoffset: 200;
        animation: dash 4s ease-out forwards;
      }}
      
      .glass-card {{
        fill: rgba(15, 23, 42, 0.4);
        stroke: rgba(255, 255, 255, 0.05);
        stroke-width: 1;
        backdrop-filter: blur(12px);
        rx: 16px;
      }}

      .title {{
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 64px;
        letter-spacing: -2.5px;
        fill: url(#text-grad);
        animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
      }}

      .subtitle {{
        font-family: 'Inter', sans-serif;
        font-weight: 400;
        font-size: 18px;
        fill: #94A3B8;
        letter-spacing: -0.2px;
        opacity: 0;
        animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) 0.3s forwards;
      }}
      
      .badge-bg {{
        fill: rgba(56, 189, 248, 0.08);
        stroke: rgba(56, 189, 248, 0.4);
        stroke-width: 1;
        rx: 12px;
        opacity: 0;
        animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
      }}
      
      .badge-text {{
        font-family: 'JetBrains Mono', monospace;
        font-size: 13px;
        font-weight: 500;
        fill: #38BDF8;
        letter-spacing: 0.5px;
        opacity: 0;
        animation: fadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) 0.6s forwards;
      }}
      
      .accent-dot {{
        fill: #38BDF8;
        animation: glow 3s infinite;
      }}

    </style>
    
    <radialGradient id="bg-grad" cx="50%" cy="0%" r="100%" fx="50%" fy="0%">
      <stop offset="0%" stop-color="#0a0a0a" />
      <stop offset="100%" stop-color="#000000" />
    </radialGradient>
    
    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" />
      <stop offset="100%" stop-color="#94A3B8" />
    </linearGradient>

    <linearGradient id="accent-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#818CF8" />
    </linearGradient>

  </defs>

  <!-- Dark Luxury Background -->
  <rect width="{width}" height="{height}" class="bg-gradient"/>
  
  <!-- Network Background Pattern -->
  <g opacity="0.9">
    {lines_svg}
    {nodes_svg}
  </g>

  <!-- Central Glassmorphism Card -->
  <g transform="translate(65, 45)">
    <rect width="720" height="230" class="glass-card" />
    
    <!-- Content inside Card -->
    <g transform="translate(60, 80)">
      
      <!-- Status Indicator -->
      <g transform="translate(0, -25)" style="opacity: 0; animation: fadeIn 1s ease 0.1s forwards;">
        <circle cx="6" cy="6" r="4" class="accent-dot" />
        <text x="18" y="10" font-family="'JetBrains Mono', monospace" font-size="12" fill="#94A3B8" letter-spacing="1">SYSTEM_ONLINE</text>
      </g>

      <!-- Main Title -->
      <text x="0" y="45" class="title">Nithissh<tspan fill="#38BDF8">.</tspan></text>
      
      <!-- Subtitle -->
      <text x="4" y="85" class="subtitle">Architecting AI systems &amp; high-performance web products.</text>
      
      <!-- Badges -->
      <g transform="translate(4, 115)">
        <rect x="0" y="0" width="165" height="26" class="badge-bg" />
        <text x="16" y="17" class="badge-text">AI / ML Engineer</text>
        
        <rect x="180" y="0" width="180" height="26" class="badge-bg" style="animation-delay: 0.7s;" />
        <text x="196" y="17" class="badge-text" style="animation-delay: 0.7s;">Full Stack Developer</text>
      </g>
    </g>
  </g>
</svg>'''

with open("animated_banner.svg", "w", encoding="utf-8") as f:
    f.write(svg)

print("Premium Neural Network SVG banner generated.")
