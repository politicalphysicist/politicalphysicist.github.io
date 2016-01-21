# Plot Settings
set xrange [:]
set yrange [:]
set xlab 'X-axis'
set ylab 'Y-axis'

# Plot Output
set term cairolatex pdf size 15cm,10cm standalone
filename = 'plot'
set output filename.'.tex'

# Variables

# Functions

# Plot Command(s)

# Produce final plot
unset output
system 'pdflatex -interaction=nonstopmode '.filename.'.tex'

# Cleanup
system 'rm *.aux; rm *.log; rm *inc.pdf'