Title: Software

I enjoy programming and have a variety of projects which I share on GitHub. A
selection of some of the most notable is described below. I mostly program in
[Fortran](http://fortranwiki.org/fortran/show/HomePage)
(for numerical projects) and [Python](https://www.python.org/) (for most other
things). I've also dabbled a bit with
[Vala](https://wiki.gnome.org/Projects/Vala), which is quite a nice language
designed for writing GTK applications.

###[Futility](https://github.com/cmacmackin/futility)
This is a collection of Fortran utilities which I have written. At the moment it
is fairly sparse, but I hope to be adding more components to it over the
summer. These will (hopefully) include a system of error-handling, routines
for manipulating paths, routines for interacting with the file-system, and some
common data structures.

###[FORD](https://github.com/cmacmackin/ford)
An automatic documentation tool for modern Fortran programs. This software
extracts information from comments and the structure of your code itself in
order to generate a set of HTML pages describing the API of your program. I
wrote it because [Doxygen](http://www.stack.nl/~dimitri/doxygen/), the most
widely used automatic documentation tool, does not work well for Fortran, while
[ROBODoc](http://rfsber.home.xs4all.nl/Robo/index.html) can not analyze the
source code at all, thus relying completely on comments. Furthermore, both
of these projects use non-standard markup languages, whereas I wanted one which
could process comments written in
[Markdown](http://daringfireball.net/projects/markdown/syntax).
Various configuration options are available for FORD and more will be added
over time.

###[markdown-include](https://github.com/cmacmackin/markdown-include)
A small extension which I wrote for
[Python-Markdown](https://pythonhosted.org/Markdown/). Originally this was
prompted by a feature request on my FORD project. It allows the contents of
an external Markdown file to be placed within those of the file being
processed.

###[backdrop-theme](https://github.com/cmacmackin/backdrop-theme)
The Pelican static site generator theme used for this blog. You can clone
the repository and generate it using [Grunt](http://gruntjs.com/) and
[Sass](http://sass-lang.com/), or you can clone the
[Pelican Themes](https://github.com/getpelican/pelican-themes) repository and
use the pre-built version available there.
