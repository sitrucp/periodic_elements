# <?xml version="1.0" encoding="utf-8"?><!--
""" To recover the Python script to generate this SVG, delete the line above -->
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="100%" height="100%" viewBox="10040 10010 1820 910">
 <title>Nucleosynthesis periodic table</title>
 <desc>Periodic table showing origin of elements in the Solar System, by CMG Lee based on http://www.astronomy.ohio-state.edu/~jaj/nucleo/ by Jennifer Johnson.</desc>
 <defs>
  <linearGradient id="grad_overlay" x1="0%" y1="0%" x2="0%" y2="100%">
   <stop offset="10%" stop-color="#ffffff" stop-opacity="0.5"/>
   <stop offset="90%" stop-color="#000000" stop-opacity="0"/>
  </linearGradient>
  <pattern id="pattern_grid_1" patternUnits="userSpaceOnUse" width="10" height="10">
   <rect x="0" y="0" width="9999" height="9999" stroke="#ffffff" stroke-width="1" fill="none"/>
  </pattern>
  <pattern id="pattern_grid_5" patternUnits="userSpaceOnUse" width="50" height="50">
   <rect x="0" y="0" width="9999" height="9999" stroke="#ffffff" stroke-width="2" fill="url(#pattern_grid_1)"/>
  </pattern>
  <pattern id="pattern_origin_y" patternUnits="userSpaceOnUse" width="10" height="10">
   <rect x="0" y="0" width="9999" height="9999" stroke="none" fill="#00cc00"/>
   <path d="M 0,-5 L 15,10 M -5,0 L 10,15" stroke-width="4" stroke="#00ff00"/>
  </pattern>
  <pattern id="pattern_origin_c" patternUnits="userSpaceOnUse" width="10" height="10">
   <rect x="0" y="0" width="9999" height="9999" stroke="none" fill="#eeeeee"/>
   <path d="M 10,-5 L -5,10 M 0,15 L 15,0" stroke-width="4" stroke="#cccccc"/>
  </pattern>
  <pattern id="pattern_origin_o" patternUnits="userSpaceOnUse" width="10" height="10">
   <rect x="0" y="0" width="9999" height="9999" stroke="none" fill="#cc99ff"/>
   <circle cx="5" cy="5" r="4" stroke-width="2" stroke="#cc66ff" fill="none"/>
  </pattern>
  <rect id="base" x="0" y="0" width="100" height="100"/>
  <g id="overlay">
   <use xlink:href="#base" fill="url(#grad_overlay)"/>
   <use xlink:href="#base" fill="url(#pattern_grid_5)" fill-opacity="0.5"/>
  </g>
  <path id="legend" d="M 10285,10050 v 250 h 930 v -150 a 40,40 0 0 1 40,-40 h 300 v -60 z" fill="#ffffff"/>
 </defs>
 <circle cx="0" cy="0" r="99999" fill="#ffffff"/>
 <g id="main" font-family="Helvetica,Arial,sans-serif" font-size="50" text-anchor="middle" stroke-linejoin="round" stroke="none" fill="#000000">
  <use xlink:href="#legend" stroke-width="50" stroke="#eeeeee"/>
  <use xlink:href="#legend" stroke-width="35" stroke="#ffffff"/>
  <path d="M 10280,10600 a 5,5 0 1 0 0,1 h 50 v 150 h 20 M 10280,10700 a 5,5 0 1 0 0,1 h 20 v 150 h 50" stroke-width="2" stroke="#000000" fill="none"/>
<!-- BEGIN_DYNAMIC_SVG { -->
  <g transform="translate(10100,10100)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#0099ff"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>H</tspan><tspan x="0" y="35" font-size="30">1</tspan></text>
   <title>100% Big Bang fusion</title>
  </g>
  <g transform="translate(11800,10100)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 7 v 10 H 0 V 10 H 0 Z" fill="#0099ff"/>
   <path d="M 7,90 H 58 v 10 H 7 Z" fill="#ffcc00"/>
   <path d="M 58,90 H 100 v 10 H 58 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>He</tspan><tspan x="0" y="35" font-size="30">2</tspan></text>
   <title>91% Big Bang fusion, 
5% Exploding massive stars, 
4% Dying low-mass stars</title>
  </g>
  <g transform="translate(10100,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 30 v 10 H 0 V 10 H 0 Z" fill="#0099ff"/>
   <path d="M 30,20 H 100 V 30 H 65 v 10 H 0 V 30 H 30 Z" fill="#ff9999"/>
   <path d="M 65,30 H 100 V 90 H 100 v 10 H 0 V 40 H 65 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Li</tspan><tspan x="0" y="35" font-size="30">3</tspan></text>
   <title>23% Big Bang fusion, 
13% Cosmic ray fission, 
64% Dying low-mass stars</title>
  </g>
  <g transform="translate(10200,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ff9999"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Be</tspan><tspan x="0" y="35" font-size="30">4</tspan></text>
   <title>100% Cosmic ray fission</title>
  </g>
  <g transform="translate(11300,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ff9999"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>B</tspan><tspan x="0" y="35" font-size="30">5</tspan></text>
   <title>100% Cosmic ray fission</title>
  </g>
  <g transform="translate(11400,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 47 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 47,20 H 100 V 90 H 100 v 10 H 0 V 30 H 47 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>C</tspan><tspan x="0" y="35" font-size="30">6</tspan></text>
   <title>25% Exploding massive stars, 
75% Dying low-mass stars</title>
  </g>
  <g transform="translate(11500,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 47 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 47,20 H 100 V 90 H 100 v 10 H 0 V 30 H 47 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>N</tspan><tspan x="0" y="35" font-size="30">7</tspan></text>
   <title>25% Exploding massive stars, 
75% Dying low-mass stars</title>
  </g>
  <g transform="translate(11600,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>O</tspan><tspan x="0" y="35" font-size="30">8</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11700,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>F</tspan><tspan x="0" y="35" font-size="30">9</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11800,10200)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ne</tspan><tspan x="0" y="35" font-size="30">10</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(10100,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Na</tspan><tspan x="0" y="35" font-size="30">11</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(10200,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 92 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 92,90 H 100 v 10 H 92 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Mg</tspan><tspan x="0" y="35" font-size="30">12</tspan></text>
   <title>99% Exploding massive stars, 
1% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11300,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 96 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 96,90 H 100 v 10 H 96 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Al</tspan><tspan x="0" y="35" font-size="30">13</tspan></text>
   <title>99.6% Exploding massive stars, 
0.4% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11400,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 70 H 5 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 5,70 H 100 V 90 H 100 v 10 H 0 V 80 H 5 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Si</tspan><tspan x="0" y="35" font-size="30">14</tspan></text>
   <title>71% Exploding massive stars, 
29% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11500,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 72 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 72,90 H 100 v 10 H 72 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>P</tspan><tspan x="0" y="35" font-size="30">15</tspan></text>
   <title>97% Exploding massive stars, 
3% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11600,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 78 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 78,50 H 100 V 90 H 100 v 10 H 0 V 60 H 78 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>S</tspan><tspan x="0" y="35" font-size="30">16</tspan></text>
   <title>58% Exploding massive stars, 
42% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11700,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 80 H 42 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 42,80 H 100 V 90 H 100 v 10 H 0 V 90 H 42 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cl</tspan><tspan x="0" y="35" font-size="30">17</tspan></text>
   <title>84% Exploding massive stars, 
16% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11800,10300)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 58 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 58,50 H 100 V 90 H 100 v 10 H 0 V 60 H 58 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ar</tspan><tspan x="0" y="35" font-size="30">18</tspan></text>
   <title>56% Exploding massive stars, 
44% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10100,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 80 H 23 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 23,80 H 100 V 90 H 100 v 10 H 0 V 90 H 23 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>K</tspan><tspan x="0" y="35" font-size="30">19</tspan></text>
   <title>82% Exploding massive stars, 
18% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10200,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 5 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 5,50 H 100 V 90 H 100 v 10 H 0 V 60 H 5 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ca</tspan><tspan x="0" y="35" font-size="30">20</tspan></text>
   <title>51% Exploding massive stars, 
49% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10300,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 80 H 23 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 23,80 H 100 V 90 H 100 v 10 H 0 V 90 H 23 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Sc</tspan><tspan x="0" y="35" font-size="30">21</tspan></text>
   <title>82% Exploding massive stars, 
18% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10400,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 46 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 46,30 H 100 V 90 H 100 v 10 H 0 V 40 H 46 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ti</tspan><tspan x="0" y="35" font-size="30">22</tspan></text>
   <title>35% Exploding massive stars, 
65% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10500,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 47 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 47,20 H 100 V 90 H 100 v 10 H 0 V 30 H 47 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>V</tspan><tspan x="0" y="35" font-size="30">23</tspan></text>
   <title>25% Exploding massive stars, 
75% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10600,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 32 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 32,20 H 100 V 90 H 100 v 10 H 0 V 30 H 32 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cr</tspan><tspan x="0" y="35" font-size="30">24</tspan></text>
   <title>23% Exploding massive stars, 
77% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10700,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 64 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 64,10 H 100 V 90 H 100 v 10 H 0 V 20 H 64 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Mn</tspan><tspan x="0" y="35" font-size="30">25</tspan></text>
   <title>16% Exploding massive stars, 
84% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10800,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 56 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 56,30 H 100 V 90 H 100 v 10 H 0 V 40 H 56 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Fe</tspan><tspan x="0" y="35" font-size="30">26</tspan></text>
   <title>36% Exploding massive stars, 
64% Exploding white dwarfs</title>
  </g>
  <g transform="translate(10900,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 29 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 29,30 H 100 V 90 H 100 v 10 H 0 V 40 H 29 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Co</tspan><tspan x="0" y="35" font-size="30">27</tspan></text>
   <title>33% Exploding massive stars, 
67% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11000,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 3 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 3,30 H 100 V 90 H 100 v 10 H 0 V 40 H 3 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ni</tspan><tspan x="0" y="35" font-size="30">28</tspan></text>
   <title>30% Exploding massive stars, 
70% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11100,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 40 H 22 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 22,40 H 100 V 90 H 100 v 10 H 0 V 50 H 22 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cu</tspan><tspan x="0" y="35" font-size="30">29</tspan></text>
   <title>42% Exploding massive stars, 
58% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11200,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 40 H 63 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 63,40 H 100 V 90 H 100 v 10 H 0 V 50 H 63 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Zn</tspan><tspan x="0" y="35" font-size="30">30</tspan></text>
   <title>46% Exploding massive stars, 
54% Exploding white dwarfs</title>
  </g>
  <g transform="translate(11300,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ga</tspan><tspan x="0" y="35" font-size="30">31</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11400,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ge</tspan><tspan x="0" y="35" font-size="30">32</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11500,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>As</tspan><tspan x="0" y="35" font-size="30">33</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11600,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Se</tspan><tspan x="0" y="35" font-size="30">34</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11700,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Br</tspan><tspan x="0" y="35" font-size="30">35</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(11800,10400)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Kr</tspan><tspan x="0" y="35" font-size="30">36</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(10100,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Rb</tspan><tspan x="0" y="35" font-size="30">37</tspan></text>
   <title>100% Exploding massive stars</title>
  </g>
  <g transform="translate(10200,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 29 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 29,10 H 100 V 90 H 100 v 10 H 0 V 20 H 29 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Sr</tspan><tspan x="0" y="35" font-size="30">38</tspan></text>
   <title>13% Exploding massive stars, 
87% Dying low-mass stars</title>
  </g>
  <g transform="translate(10300,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 80 v 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 80,0 H 100 V 90 H 100 v 10 H 0 V 10 H 80 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Y</tspan><tspan x="0" y="35" font-size="30">39</tspan></text>
   <title>8% Exploding massive stars, 
92% Dying low-mass stars</title>
  </g>
  <g transform="translate(10400,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 64 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
   <path d="M 64,10 H 100 V 90 H 100 v 10 H 0 V 20 H 64 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Zr</tspan><tspan x="0" y="35" font-size="30">40</tspan></text>
   <title>16% Exploding massive stars, 
84% Dying low-mass stars</title>
  </g>
  <g transform="translate(10500,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 80 H 65 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 65,80 H 100 V 90 H 100 v 10 H 0 V 90 H 65 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Nb</tspan><tspan x="0" y="35" font-size="30">41</tspan></text>
   <title>87% Dying low-mass stars, 
13% Merging neutron stars</title>
  </g>
  <g transform="translate(10600,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 60 H 26 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 26,60 H 100 V 90 H 100 v 10 H 0 V 70 H 26 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Mo</tspan><tspan x="0" y="35" font-size="30">42</tspan></text>
   <title>63% Dying low-mass stars, 
37% Merging neutron stars</title>
  </g>
  <g transform="translate(10700,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Tc</tspan><tspan x="0" y="35" font-size="30">43</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(10800,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 20 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 20,30 H 100 V 90 H 100 v 10 H 0 V 40 H 20 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ru</tspan><tspan x="0" y="35" font-size="30">44</tspan></text>
   <title>32% Dying low-mass stars, 
68% Merging neutron stars</title>
  </g>
  <g transform="translate(10900,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 35 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 35,10 H 100 V 90 H 100 v 10 H 0 V 20 H 35 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Rh</tspan><tspan x="0" y="35" font-size="30">45</tspan></text>
   <title>13% Dying low-mass stars, 
87% Merging neutron stars</title>
  </g>
  <g transform="translate(11000,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 40 H 53 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 53,40 H 100 V 90 H 100 v 10 H 0 V 50 H 53 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pd</tspan><tspan x="0" y="35" font-size="30">46</tspan></text>
   <title>45% Dying low-mass stars, 
55% Merging neutron stars</title>
  </g>
  <g transform="translate(11100,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 90 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 90,10 H 100 V 90 H 100 v 10 H 0 V 20 H 90 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ag</tspan><tspan x="0" y="35" font-size="30">47</tspan></text>
   <title>19% Dying low-mass stars, 
81% Merging neutron stars</title>
  </g>
  <g transform="translate(11200,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 16 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 16,50 H 100 V 90 H 100 v 10 H 0 V 60 H 16 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cd</tspan><tspan x="0" y="35" font-size="30">48</tspan></text>
   <title>52% Dying low-mass stars, 
48% Merging neutron stars</title>
  </g>
  <g transform="translate(11300,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 56 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 56,30 H 100 V 90 H 100 v 10 H 0 V 40 H 56 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>In</tspan><tspan x="0" y="35" font-size="30">49</tspan></text>
   <title>36% Dying low-mass stars, 
64% Merging neutron stars</title>
  </g>
  <g transform="translate(11400,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 60 H 89 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 89,60 H 100 V 90 H 100 v 10 H 0 V 70 H 89 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Sn</tspan><tspan x="0" y="35" font-size="30">50</tspan></text>
   <title>69% Dying low-mass stars, 
31% Merging neutron stars</title>
  </g>
  <g transform="translate(11500,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 55 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 55,20 H 100 V 90 H 100 v 10 H 0 V 30 H 55 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Sb</tspan><tspan x="0" y="35" font-size="30">51</tspan></text>
   <title>25% Dying low-mass stars, 
75% Merging neutron stars</title>
  </g>
  <g transform="translate(11600,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 68 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 68,50 H 100 V 90 H 100 v 10 H 0 V 60 H 68 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Te</tspan><tspan x="0" y="35" font-size="30">52</tspan></text>
   <title>57% Dying low-mass stars, 
43% Merging neutron stars</title>
  </g>
  <g transform="translate(11700,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 46 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 46,0 H 100 V 90 H 100 v 10 H 0 V 10 H 46 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>I</tspan><tspan x="0" y="35" font-size="30">53</tspan></text>
   <title>5% Dying low-mass stars, 
95% Merging neutron stars</title>
  </g>
  <g transform="translate(11800,10500)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 70 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 70,10 H 100 V 90 H 100 v 10 H 0 V 20 H 70 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Xe</tspan><tspan x="0" y="35" font-size="30">54</tspan></text>
   <title>17% Dying low-mass stars, 
83% Merging neutron stars</title>
  </g>
  <g transform="translate(10100,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 52 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 52,10 H 100 V 90 H 100 v 10 H 0 V 20 H 52 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cs</tspan><tspan x="0" y="35" font-size="30">55</tspan></text>
   <title>15% Dying low-mass stars, 
85% Merging neutron stars</title>
  </g>
  <g transform="translate(10200,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 80 H 17 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 17,80 H 100 V 90 H 100 v 10 H 0 V 90 H 17 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ba</tspan><tspan x="0" y="35" font-size="30">56</tspan></text>
   <title>82% Dying low-mass stars, 
18% Merging neutron stars</title>
  </g>
  <g transform="translate(10400,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 60 H 17 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 17,60 H 100 V 90 H 100 v 10 H 0 V 70 H 17 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>La</tspan><tspan x="0" y="35" font-size="30">57</tspan></text>
   <title>62% Dying low-mass stars, 
38% Merging neutron stars</title>
  </g>
  <g transform="translate(10500,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 70 H 61 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 61,70 H 100 V 90 H 100 v 10 H 0 V 80 H 61 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ce</tspan><tspan x="0" y="35" font-size="30">58</tspan></text>
   <title>76% Dying low-mass stars, 
24% Merging neutron stars</title>
  </g>
  <g transform="translate(10600,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 40 H 84 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 84,40 H 100 V 90 H 100 v 10 H 0 V 50 H 84 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pr</tspan><tspan x="0" y="35" font-size="30">59</tspan></text>
   <title>48% Dying low-mass stars, 
52% Merging neutron stars</title>
  </g>
  <g transform="translate(10700,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 97 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 97,50 H 100 V 90 H 100 v 10 H 0 V 60 H 97 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Nd</tspan><tspan x="0" y="35" font-size="30">60</tspan></text>
   <title>60% Dying low-mass stars, 
40% Merging neutron stars</title>
  </g>
  <g transform="translate(10800,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pm</tspan><tspan x="0" y="35" font-size="30">61</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(10900,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 20 H 95 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 95,20 H 100 V 90 H 100 v 10 H 0 V 30 H 95 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Sm</tspan><tspan x="0" y="35" font-size="30">62</tspan></text>
   <title>29% Dying low-mass stars, 
71% Merging neutron stars</title>
  </g>
  <g transform="translate(11000,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 53 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 53,0 H 100 V 90 H 100 v 10 H 0 V 10 H 53 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Eu</tspan><tspan x="0" y="35" font-size="30">63</tspan></text>
   <title>5% Dying low-mass stars, 
95% Merging neutron stars</title>
  </g>
  <g transform="translate(11100,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 46 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 46,10 H 100 V 90 H 100 v 10 H 0 V 20 H 46 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Gd</tspan><tspan x="0" y="35" font-size="30">64</tspan></text>
   <title>15% Dying low-mass stars, 
85% Merging neutron stars</title>
  </g>
  <g transform="translate(11200,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 68 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 68,0 H 100 V 90 H 100 v 10 H 0 V 10 H 68 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Tb</tspan><tspan x="0" y="35" font-size="30">65</tspan></text>
   <title>7% Dying low-mass stars, 
93% Merging neutron stars</title>
  </g>
  <g transform="translate(11300,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 40 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 40,10 H 100 V 90 H 100 v 10 H 0 V 20 H 40 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Dy</tspan><tspan x="0" y="35" font-size="30">66</tspan></text>
   <title>14% Dying low-mass stars, 
86% Merging neutron stars</title>
  </g>
  <g transform="translate(11400,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 72 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 72,0 H 100 V 90 H 100 v 10 H 0 V 10 H 72 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ho</tspan><tspan x="0" y="35" font-size="30">67</tspan></text>
   <title>7% Dying low-mass stars, 
93% Merging neutron stars</title>
  </g>
  <g transform="translate(11500,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 64 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 64,10 H 100 V 90 H 100 v 10 H 0 V 20 H 64 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Er</tspan><tspan x="0" y="35" font-size="30">68</tspan></text>
   <title>16% Dying low-mass stars, 
84% Merging neutron stars</title>
  </g>
  <g transform="translate(11600,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 24 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 24,10 H 100 V 90 H 100 v 10 H 0 V 20 H 24 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Tm</tspan><tspan x="0" y="35" font-size="30">69</tspan></text>
   <title>12% Dying low-mass stars, 
88% Merging neutron stars</title>
  </g>
  <g transform="translate(11700,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 30 H 20 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 20,30 H 100 V 90 H 100 v 10 H 0 V 40 H 20 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Yb</tspan><tspan x="0" y="35" font-size="30">70</tspan></text>
   <title>32% Dying low-mass stars, 
68% Merging neutron stars</title>
  </g>
  <g transform="translate(11800,10750)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 10 H 97 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 97,10 H 100 V 90 H 100 v 10 H 0 V 20 H 97 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Lu</tspan><tspan x="0" y="35" font-size="30">71</tspan></text>
   <title>20% Dying low-mass stars, 
80% Merging neutron stars</title>
  </g>
  <g transform="translate(10400,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 47 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 47,50 H 100 V 90 H 100 v 10 H 0 V 60 H 47 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Hf</tspan><tspan x="0" y="35" font-size="30">72</tspan></text>
   <title>55% Dying low-mass stars, 
45% Merging neutron stars</title>
  </g>
  <g transform="translate(10500,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 40 H 12 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 12,40 H 100 V 90 H 100 v 10 H 0 V 50 H 12 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ta</tspan><tspan x="0" y="35" font-size="30">73</tspan></text>
   <title>41% Dying low-mass stars, 
59% Merging neutron stars</title>
  </g>
  <g transform="translate(10600,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 50 H 68 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 68,50 H 100 V 90 H 100 v 10 H 0 V 60 H 68 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>W</tspan><tspan x="0" y="35" font-size="30">74</tspan></text>
   <title>57% Dying low-mass stars, 
43% Merging neutron stars</title>
  </g>
  <g transform="translate(10700,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 84 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 84,0 H 100 V 90 H 100 v 10 H 0 V 10 H 84 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Re</tspan><tspan x="0" y="35" font-size="30">75</tspan></text>
   <title>8% Dying low-mass stars, 
92% Merging neutron stars</title>
  </g>
  <g transform="translate(10800,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 98 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 98,0 H 100 V 90 H 100 v 10 H 0 V 10 H 98 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Os</tspan><tspan x="0" y="35" font-size="30">76</tspan></text>
   <title>10% Dying low-mass stars, 
90% Merging neutron stars</title>
  </g>
  <g transform="translate(10900,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 15 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 15,0 H 100 V 90 H 100 v 10 H 0 V 10 H 15 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ir</tspan><tspan x="0" y="35" font-size="30">77</tspan></text>
   <title>1% Dying low-mass stars, 
99% Merging neutron stars</title>
  </g>
  <g transform="translate(11000,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 53 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 53,0 H 100 V 90 H 100 v 10 H 0 V 10 H 53 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pt</tspan><tspan x="0" y="35" font-size="30">78</tspan></text>
   <title>5% Dying low-mass stars, 
95% Merging neutron stars</title>
  </g>
  <g transform="translate(11100,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 60 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 60,0 H 100 V 90 H 100 v 10 H 0 V 10 H 60 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Au</tspan><tspan x="0" y="35" font-size="30">79</tspan></text>
   <title>6% Dying low-mass stars, 
94% Merging neutron stars</title>
  </g>
  <g transform="translate(11200,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 60 H 17 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 17,60 H 100 V 90 H 100 v 10 H 0 V 70 H 17 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Hg</tspan><tspan x="0" y="35" font-size="30">80</tspan></text>
   <title>62% Dying low-mass stars, 
38% Merging neutron stars</title>
  </g>
  <g transform="translate(11300,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 70 H 68 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 68,70 H 100 V 90 H 100 v 10 H 0 V 80 H 68 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Tl</tspan><tspan x="0" y="35" font-size="30">81</tspan></text>
   <title>77% Dying low-mass stars, 
23% Merging neutron stars</title>
  </g>
  <g transform="translate(11400,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 40 H 73 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 73,40 H 100 V 90 H 100 v 10 H 0 V 50 H 73 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pb</tspan><tspan x="0" y="35" font-size="30">82</tspan></text>
   <title>47% Dying low-mass stars, 
53% Merging neutron stars</title>
  </g>
  <g transform="translate(11500,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 5 v 10 H 0 Z" fill="url(#pattern_origin_y)"/>
   <path d="M 5,0 H 100 V 90 H 100 v 10 H 0 V 10 H 5 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Bi</tspan><tspan x="0" y="35" font-size="30">83</tspan></text>
   <title>0.5% Dying low-mass stars, 
99.5% Merging neutron stars</title>
  </g>
  <g transform="translate(11600,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Po</tspan><tspan x="0" y="35" font-size="30">84</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(11700,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>At</tspan><tspan x="0" y="35" font-size="30">85</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(11800,10600)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Rn</tspan><tspan x="0" y="35" font-size="30">86</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10100,10700)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Fr</tspan><tspan x="0" y="35" font-size="30">87</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10200,10700)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ra</tspan><tspan x="0" y="35" font-size="30">88</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10400,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Ac</tspan><tspan x="0" y="35" font-size="30">89</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10500,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Th</tspan><tspan x="0" y="35" font-size="30">90</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10600,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pa</tspan><tspan x="0" y="35" font-size="30">91</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10700,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>U</tspan><tspan x="0" y="35" font-size="30">92</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10800,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Np</tspan><tspan x="0" y="35" font-size="30">93</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(10900,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Pu</tspan><tspan x="0" y="35" font-size="30">94</tspan></text>
   <title>100% Merging neutron stars</title>
  </g>
  <g transform="translate(11000,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Am</tspan><tspan x="0" y="35" font-size="30">95</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11100,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cm</tspan><tspan x="0" y="35" font-size="30">96</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11200,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Bk</tspan><tspan x="0" y="35" font-size="30">97</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11300,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Cf</tspan><tspan x="0" y="35" font-size="30">98</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11400,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Es</tspan><tspan x="0" y="35" font-size="30">99</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11500,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Fm</tspan><tspan x="0" y="35" font-size="30">100</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11600,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Md</tspan><tspan x="0" y="35" font-size="30">101</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11700,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>No</tspan><tspan x="0" y="35" font-size="30">102</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(11800,10850)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text x="0" y="0"><tspan>Lr</tspan><tspan x="0" y="35" font-size="30">103</tspan></text>
   <title>100% Human synthesis No stable isotopes</title>
  </g>
  <g transform="translate(10325,10090)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#0099ff"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Big</tspan><tspan x="0" dy="40">Bang</tspan><tspan x="0" dy="40">fusion</tspan></text>
  </g>
  <g transform="translate(10325,10240)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ff9999"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Cosmic</tspan><tspan x="0" dy="40">ray</tspan><tspan x="0" dy="40">fission</tspan></text>
  </g>
  <g transform="translate(10580,10090)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_y)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Dying</tspan><tspan x="0" dy="40">low-mass</tspan><tspan x="0" dy="40">stars</tspan></text>
  </g>
  <g transform="translate(10580,10240)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_o)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Merging</tspan><tspan x="0" dy="40">neutron</tspan><tspan x="0" dy="40">stars</tspan></text>
  </g>
  <g transform="translate(10870,10090)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#ffcc00"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Exploding</tspan><tspan x="0" dy="40">massive</tspan><tspan x="0" dy="40">stars</tspan></text>
  </g>
  <g transform="translate(10870,10240)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="url(#pattern_origin_c)"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Exploding</tspan><tspan x="0" dy="40">white</tspan><tspan x="0" dy="40">dwarfs</tspan></text>
  </g>
  <g transform="translate(11170,10090)" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
   <path d="M 0,0 H 100 V 90 H 100 v 10 H 0 V 10 H 0 Z" fill="#999966"/>
    <use xlink:href="#overlay"/>
   </g>
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>Human synthesis</tspan><tspan x="0" dy="40">No stable isotopes</tspan></text>
  </g>
<!-- } END_DYNAMIC_SVG -->
 </g>
</svg>
<!-- Please retain this and other comments, which contain Python code to generate this SVG. """
import re, math, collections, json, pandas as pd

def fmt(string): ## string.format(**vars()) using tags {expression!format} by CMG Lee
 def f(tag): i_sep = tag.rfind('!'); return (re.sub('\.0+$', '', str(eval(tag[1:-1])))
  if (i_sep < 0) else ('{:%s}' % tag[i_sep + 1:-1]).format(eval(tag[1:i_sep])))
 return (re.sub(r'(?<!{){[^{}]+}', lambda m:f(m.group()), string)
         .replace('{{', '{').replace('}}', '}'))
def append(obj, string): return obj.append(fmt(string))
def format_tab(*arg): return '\t'.join([str(el) for el in (arg if len(arg) > 1 else arg[0])])

def get_shading_x_y(fraction):
 fraction10 = fraction * 10
 y = int(fraction10)
 x = fraction10 - y
 return (int(x * 100 + 0.5), y * 10)

datass = [[field.strip() for field in line.split('|')] for line in '''
H | 1  |1  |0  |b
He|18  |1  |40 |ygb
Li| 1  |2  |79 |jby
Be| 2  |2  |0  |j
B |13  |2  |0  |j
C |14  |2  |65 |gy
N |15  |2  |65 |gy
O |16  |2  |0  |g
F |17  |2  |0  |g
Ne|18  |2  |0  |g
Na| 1  |3  |0  |g
Mg| 2  |3  |173|gc
Al|13  |3  |177|gc
Si|14  |3  |114|gc
P |15  |3  |163|gc
S |16  |3  |100|gc
Cl|17  |3  |133|gc
Ar|18  |3  |98 |gc
K | 1  |4  |130|gc
Ca| 2  |4  |93 |gc
Sc| 3  |4  |130|gc
Ti| 4  |4  |77 |gc
V | 5  |4  |65 |gc
Cr| 6  |4  |63 |gc
Mn| 7  |4  |53 |gc
Fe| 8  |4  |78 |gc
Co| 9  |4  |75 |gc
Ni|10  |4  |72 |gc
Cu|11  |4  |85 |gc
Zn|12  |4  |89 |gc
Ga|13  |4  |0  |g
Ge|14  |4  |0  |g
As|15  |4  |0  |g
Se|16  |4  |0  |g
Br|17  |4  |0  |g
Kr|18  |4  |0  |g
Rb| 1  |5  |0  |g
Sr| 2  |5  |47 |gy
Y | 3  |5  |37 |gy
Zr| 4  |5  |53 |gy
Nb| 5  |5  |48 |oy
Mo| 6  |5  |80 |oy
Tc| 7  |5  |0  |z
Ru| 8  |5  |111|oy
Rh| 9  |5  |137|oy
Pd|10  |5  |97 |oy
Ag|11  |5  |128|oy
Cd|12  |5  |91 |oy
In|13  |5  |107|oy
Sn|14  |5  |73 |oy
Sb|15  |5  |119|oy
Te|16  |5  |86 |oy
I |17  |5  |157|oy
Xe|18  |5  |131|oy
Cs| 1  |6  |134|oy
Ba| 2  |6  |56 |oy
La| 4  |7.5|81 |oy
Ce| 5  |7.5|64 |oy
Pr| 6  |7.5|94 |oy
Nd| 7  |7.5|83 |oy
Pm| 8  |7.5|0  |z
Sm| 9  |7.5|114|oy
Eu|10  |7.5|155|oy
Gd|11  |7.5|135|oy
Tb|12  |7.5|151|oy
Dy|13  |7.5|136|oy
Ho|14  |7.5|150|oy
Er|15  |7.5|132|oy
Tm|16  |7.5|139|oy
Yb|17  |7.5|111|oy
Lu|18  |7.5|127|oy
Hf| 4  |6  |88 |oy
Ta| 5  |6  |101|oy
W | 6  |6  |86 |oy
Re| 7  |6  |147|oy
Os| 8  |6  |144|oy
Ir| 9  |6  |169|oy
Pt|10  |6  |155|oy
Au|11  |6  |153|oy
Hg|12  |6  |81 |oy
Tl|13  |6  |63 |oy
Pb|14  |6  |95 |oy
Bi|15  |6  |176|oy
Po|16  |6  |0  |o
At|17  |6  |0  |o
Rn|18  |6  |0  |o
Fr| 1  |7  |0  |o
Ra| 2  |7  |0  |o
Ac| 4  |8.5|0  |o
Th| 5  |8.5|0  |o
Pa| 6  |8.5|0  |o
U | 7  |8.5|0  |o
Np| 8  |8.5|0  |o
Pu| 9  |8.5|0  |o
Am|10  |8.5|0  |z
Cm|11  |8.5|0  |z
Bk|12  |8.5|0  |z
Cf|13  |8.5|0  |z
Es|14  |8.5|0  |z
Fm|15  |8.5|0  |z
Md|16  |8.5|0  |z
No|17  |8.5|0  |z
Lr|18  |8.5|0  |z
  |3.25|0.9|0  |b|Big~Bang~fusion
  |3.25|2.4|0  |j|Cosmic~ray~fission
  | 5.8|0.9|0  |y|Dying~low-mass~stars
  | 5.8|2.4|0  |o|Merging~neutron~stars
  | 8.7|0.9|0  |g|Exploding~massive~stars
  | 8.7|2.4|0  |c|Exploding~white~dwarfs
  |11.7|0.9|0  |z|Human synthesis~No stable isotopes
'''.strip('\n').split('\n')]
colours = collections.OrderedDict([('b','#0099ff'),('j','#ff9999'),('g','#ffcc00'),('c','url(#pattern_origin_c)'),
                                   ('y','url(#pattern_origin_y)'),('o','url(#pattern_origin_o)'),('z','#999966')])
x_max   = 185

origins = {}
for fields in datass:
 if (len(fields) == 6): origins[fields[4]] = fields[5].replace('~', ' ')

## i added this
list_elements = []
## to here

outs = []
for i_field in range(len(datass)):
 fields        = datass[i_field]
 atomic        = i_field + 1
 symbol        = fields[0]
 (col, row, x) = [float(field) for field in fields[1:4]]
 if (col == 0 and row == 0): continue ## skip Synthetic legend
 codes         = list(fields[4]) ## split string into list of its characters
 n_code        = len(codes)
 if ((x == 0) != (n_code == 1)): raise
 fraction  = (2 * x * x if x * 2 < x_max else 4 * x * x_max - 2 * x * x - x_max * x_max) / float(x_max * x_max)
 fractions = ([1.0] if n_code == 1 else
              ([fraction, 1.0 - fraction] if n_code == 2 else
               ([fraction * 0.45, fraction * 0.55, 1.0 - fraction] if atomic == 2 else
                [fraction * 0.37, fraction * 0.63, 1.0 - fraction])))
 format_percent = '%.0f'
 for fraction in fractions:
  if (fraction < 0.005): format_percent = '%.1f' ## ensure no 0% xx, 100% yy
 #print(format_tab(atomic, symbol, col, row, x, codes, ['%.3f' % (x) for x in fractions], format_percent))

 ## i added this
 list_elements.append([atomic, symbol, col, row, x, codes, ['%.3f' % (x) for x in fractions], format_percent])
## to here

 cumulative     = 0
 code_fractions = {}
 out_tooltips   = []
 out_shading    = []
 for code in colours:
  if code in codes: ## element has code
   code_fractions[code] = fractions[codes.index(code)]
   out_percent          = format_percent % (code_fractions[code] * 100)
   append(out_tooltips, '''{out_percent}% {origins[code]}''')
   colour               = colours[code]
   (x_begin, y_begin)   = get_shading_x_y(cumulative)
   cumulative          += code_fractions[code]
   (x_end  , y_end  )   = get_shading_x_y(cumulative)
   if (x_end == 0): x_end = 100; y_end -= 10 ## back to end of previous row if right at start of one
   if (y_begin == y_end): ## region starts and ends on the same row
    append(out_shading, '''\
   <path d="M {x_begin},{y_begin} H {x_end} v 10 H {x_begin} Z" fill="{colour}"/>''')
   else: ## region starts and ends on different rows
    append(out_shading, '''\
   <path d="M {x_begin},{y_begin} H 100 V {y_end} H {x_end} v 10 H 0 V {y_begin + 10} H {x_begin} Z" fill="{colour}"/>''')
  else: ## element does not have code
   code_fractions[code] = 0
 if (symbol == ''): ## legend
  out_legend = fields[5].replace('~', '</tspan><tspan x="0" dy="40">')
  out_label  = fmt('''\
   <text transform="translate(60,-18)" x="0" y="0" font-size="40" text-anchor="start"><tspan>{out_legend}</tspan></text>''')
 else: ## table cell
  out_label  = fmt('''\
   <text x="0" y="0"><tspan>{symbol}</tspan><tspan x="0" y="35" font-size="30">{atomic}</tspan></text>
   <title>{', \\n'.join(out_tooltips)}</title>''')
 append(outs, '''\
  <g transform="translate({col*100+10000},{row*100+10000})" cursor="help">
   <g transform="scale(0.96) translate(-50,-50)">
{'\\n'.join(out_shading)}
    <use xlink:href="#overlay"/>
   </g>
{out_label}
  </g>''')

## i added this
df_elements = pd.DataFrame(list_elements)
df_elements.columns = ['number', 'symbol', 'chart_col', 'chart_row', 'chart_x', 'source', 'percent', 'format_percent']
#print(df_elements.head(5))
## to here

out_p = 'width="100%" height="100%" viewBox="10040 10010 1820 910"'
## Compile everything into an .svg file
myself   = open(__file__, 'r').read() ## the contents of this very file
file_out = open(__file__[:__file__.rfind('.')] + '.svg', 'w') ## *.* -> *.svg
try: ## use try/finally so that file is closed even if write fails
 file_out.write('''<?xml version="1.0" encoding="utf-8"?><!%s
%s%s%s\n%s%s''' % ('-' + '-', ## because SVG comments cannot have 2 consecutive '-'s
  myself[ : myself.find('width',myself.find('<svg'))], ## assume width specified before height/viewBox
  out_p, ## replace SVG width/height/viewBox with {out_p} & dynamic SVG block with {outs} contents
  myself[myself.find('>',myself.find('<svg')) : myself.find('\n',myself.find('BEGIN_'+'DYNAMIC_SVG'))],
  '\n'.join(outs), myself[myself.rfind('\n',0,myself.find('END_'+'DYNAMIC_SVG')) : ]))
finally:
 file_out.close()

## SVG-Python near-polyglot framework version 2 by CMG Lee (Feb 2016) -->

## i added everything below
def split_dataframe_rows(df, column_selectors, row_delimiter):
    # we need to keep track of the ordering of the columns
    def _split_list_to_rows(row,row_accumulator,column_selector,row_delimiter):
        split_rows = {}
        max_split = 0
        for column_selector in column_selectors:
            split_row = row[column_selector].split(row_delimiter)
            split_rows[column_selector] = split_row
            if len(split_row) > max_split:
                max_split = len(split_row)
            
        for i in range(max_split):
            new_row = row.to_dict()
            for column_selector in column_selectors:
                try:
                    new_row[column_selector] = split_rows[column_selector].pop(0)
                except IndexError:
                    new_row[column_selector] = ''
            row_accumulator.append(new_row)

    new_rows = []
    df.apply(_split_list_to_rows,axis=1,args = (new_rows,column_selectors,row_delimiter))
    new_df = pd.DataFrame(new_rows, columns=df.columns)
    return new_df

# get count of source for element
df_elements['source_count'] = df_elements['source'].str.len()

# create string instead of list to use in split_dataframe_rows function
df_elements['source_str'] = [','.join(map(str, l)) for l in df_elements['source']]
df_elements['percent_str'] = [','.join(map(str, l)) for l in df_elements['percent']]



# use function split_dataframe_rows to split col vals into rows
df_elements_split = split_dataframe_rows(df_elements, ('source_str','percent_str'), ',')

## replace alpha character with words from source_dict
source_dict = {'b': 'Big Bang fusion','c': 'Exploding white dwarfs','g': 'Exploding massive stars','j': 'Cosmic ray fission','o': 'Merging neutron stars','y': 'Dying low-mass stars', 'z': 'Human synthesis'}
df_elements_split['source_word'] = df_elements_split['source_str'].replace(source_dict)

# write to csv
df_elements_split.to_csv('periodic_elements.csv', sep=',', encoding='utf-8')

# transform pandas dataframe into dictionary to write as json
json_elements_split = df_elements_split.to_dict('records')

# write new montreal covid_data to json file
with open('periodic_elements.json', 'w', encoding='utf8') as f:
    f.write('var periodic_elements = \n')
    json.dump(json_elements_split, f, ensure_ascii=False, indent=4)

