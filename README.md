**Periodic Chart Elements by Origin**

TLDR: View Plotly.js charts here <a href="https://sitrucp.github.io/periodic_elements/" target="_blank">https://sitrucp.github.io/periodic_elements/</a>

The very cool SVG periodic chart on wikipedia <a href="https://en.wikipedia.org/wiki/File:Nucleosynthesis_periodic_table.svg" target="_blank">https://en.wikipedia.org/wiki/File:Nucleosynthesis_periodic_table.svg</a> shows periodic elements by their origins: 

{'b': 'Big Bang fusion',
'c': 'Exploding white dwarfs',
'g': 'Exploding massive stars',
'j': 'Cosmic ray fission',
'o': 'Merging neutron stars',
'y': 'Dying low-mass stars', 
'z': 'Human synthesis'}

I wanted to get counts of elements by origin, and counts of elements by number of origin. I thought I might have to do some manual data entry from chart but it turned out the SVG file contains Python code that creates the SVG!

I modified the Python code to create a Pandas dataframe with the periodic elements, their origin source, and fractions thereof, and then export dataframe into csv and JSON files.

The code modifications additionally split column values into rows for elements that have more than one origin source. Some elements have only one origin, while others may have more than one origin. Therefore, elements with more than one origin have corresponding additional rows in the csv and JSON output file. 

For example Helium (He) was split into three rows, one for each origin eg 90% of Helium is from Big Bang fusion with small fractions from Exploding massive stars and Dying low-mass stars.

Helium (He) origin fractions:
Big Bang fusion (b) = 0.907
Exploding massive stars (g) = 0.051
Dying low-mass stars (y) = 0.042

The output was used to create two Plotly.js charts showing counts of elements by origin, and counts of elements by number of origin.
