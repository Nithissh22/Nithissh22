import random
import math

width = 800
height = 300
num_nodes = 50
max_distance = 150

nodes = []
for i in range(num_nodes):
    x = random.randint(0, width)
    y = random.randint(0, height)
    delay = random.uniform(0, 3)
    nodes.append((x, y, delay))

svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">
  <defs>
    <linearGradient id="bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#020617"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="textGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#c084fc"/>
    </linearGradient>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@700&amp;family=Inter:wght@400;600&amp;display=swap');
      
      @keyframes float {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-10px); }}
      }}
      @keyframes pulse {{
        0%, 100% {{ opacity: 0.2; r: 2; }}
        50% {{ opacity: 1; r: 4; fill: #38bdf8; filter: drop-shadow(0 0 5px #38bdf8); }}
      }}
      @keyframes dataFlow {{
        0% {{ stroke-dashoffset: 200; opacity: 0; }}
        20% {{ opacity: 1; }}
        80% {{ opacity: 1; }}
        100% {{ stroke-dashoffset: 0; opacity: 0; }}
      }}
      @keyframes typing {{
        from {{ width: 0; }}
        to {{ width: 100%; }}
      }}
      .bg-rect {{ fill: url(#bg); }}
      .connection {{ stroke: #1e293b; stroke-width: 1; opacity: 0.5; }}
      .data {{ 
        stroke: url(#textGrad); 
        stroke-width: 1.5; 
        stroke-dasharray: 10 190; 
      }}
      .node {{ fill: #475569; }}
      .title-container {{ animation: float 6s ease-in-out infinite; }}
      .title {{
        font-family: 'Fira Code', monospace;
        font-size: 64px;
        font-weight: 700;
        fill: #ffffff;
        text-anchor: middle;
      }}
      .subtitle {{
        font-family: 'Inter', sans-serif;
        font-size: 16px;
        font-weight: 400;
        fill: #94a3b8;
        text-anchor: middle;
        letter-spacing: 4px;
      }}
      .highlight {{ fill: url(#textGrad); }}
    </style>
  </defs>

  <rect width="{width}" height="{height}" class="bg-rect" rx="15"/>
  
  <g class="network">
"""

# Generate connections
for i in range(num_nodes):
    x1, y1, delay1 = nodes[i]
    # Keep center somewhat clear for text
    if 250 < x1 < 550 and 100 < y1 < 200:
        continue
        
    for j in range(i + 1, num_nodes):
        x2, y2, delay2 = nodes[j]
        if 250 < x2 < 550 and 100 < y2 < 200:
            continue
            
        dist = math.hypot(x2 - x1, y2 - y1)
        if dist < max_distance:
            svg_content += f'    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="connection" />\n'
            
            # 30% chance to add a flowing data packet
            if random.random() < 0.3:
                duration = random.uniform(2, 5)
                anim_delay = random.uniform(0, 5)
                svg_content += f'    <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="data" style="animation: dataFlow {duration}s linear infinite {anim_delay}s;" />\n'

# Generate nodes
for x, y, delay in nodes:
    if 250 < x < 550 and 100 < y < 200:
        continue
    svg_content += f'    <circle cx="{x}" cy="{y}" r="2" class="node" style="animation: pulse 3s infinite {delay}s;" />\n'

svg_content += """
  </g>

  <!-- Text overlay -->
  <g class="title-container" transform="translate(400, 150)">
    <!-- Simulated glowing box behind text -->
    <rect x="-200" y="-60" width="400" height="120" fill="#020617" opacity="0.7" rx="10" />
    <text y="10" class="title">NITHISSH<tspan class="highlight">.</tspan></text>
    <text y="40" class="subtitle">AI/ML ENGINEER &amp; FULL-STACK</text>
  </g>
</svg>
"""

with open("animated_banner.svg", "w") as f:
    f.write(svg_content)
