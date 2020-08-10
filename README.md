Periodic chart elements by origin

Periodic element origins: 
{'b': 'Big Bang fusion',
'c': 'Exploding white dwarfs',
'g': 'Exploding massive stars',
'j': 'Cosmic ray fission',
'o': 'Merging neutron stars',
'y': 'Dying low-mass stars', 
'z': 'Human synthesis'}

From <a href="https://en.wikipedia.org/wiki/File:Nucleosynthesis_periodic_table.svg" target="_blank">https://en.wikipedia.org/wiki/File:Nucleosynthesis_periodic_table.svg</a> SVG file which contains Python code to create the SVG.

I modified the Python code, used to create the SVG, to additionally to create a Pandas dataframe with the periodic elements, their origin source, and fractions thereof, and then export dataframe into csv and JSON files.

The code additionally splits column values into rows for elements that have more than one origin source. Some elements have only one origin, while others may have more than one origin. Therefore, elements with more than one origin have corresponding additional rows in the csv and JSON output file. 

For example Helium (He) was split into three rows, one for each origin eg 90% of Helium is from Big Bang fusion with small fractions from Exploding massive stars and Dying low-mass stars.

Helium (He) origin fractions:
Big Bang fusion (b) = 0.907
Exploding massive stars (g) = 0.051
Dying low-mass stars (y) = 0.042

This was done to allow creating counts of elements by origin, and counts of elements by number of origin.

See charts here <a href="https://sitrucp.github.io/periodic_elements/" target="_blank">https://sitrucp.github.io/periodic_elements/</a>





