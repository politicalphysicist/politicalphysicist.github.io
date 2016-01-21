Title: What I Did Over Christmas Break
Date: 2013-12-21 2:00
Tags: Programming, VLC, Python, GTK+, Conetroller
Summary: Thanks to the wonders of the Internet I now watch almost all movies and TV shows via my computer using an HDMI cable to play them on my television set. The problem with this arrangement is that it prevents me from using my computer for anything else while the video is playing. So, with the extra time I have over the Christmas break I set to work designing a program that, when paired with a Raspberry Pi will allow me to over come this. I present to you: Conetroller.

_If you are impatient and don't want to read my no doubt fascinating
account of the inspiration for and development process of the 
software I've designed, you can skip down to [here](#software) to read what
it does and how to install it._

![Conetroller icon](|filename|/images/conetroller-icon.svg)

One of the many great things about Christmas time is the lack of homework.
It means that I finally have the chance to work on some of the little
personal projects that I've been wanting to do. One such project, of course,
is writing some blog posts. The other major project is the subject of this
post.

Thanks to the wonders of the Internet I now watch almost all movies and TV
shows on my computer. (And no, I am not downloading them illegally.) Well,
I say on my computer: actually _via_ my computer would be more accurate, as
I use an HDMI cable to play them on my television set. The problem with this arrangement is that it prevents me from using my computer for anything
else while the video is playing because:

1. The two monitor display features on my computer leave something to be
desired.
2. My computer has to stay on my desk, connected to the HDMI cable, which
is a terribly angle to actually see the TV from.

However, it so happens that I have a spare [Raspberry Pi](http://www.raspberrypi.org/) 
(a cheap mini-computer, one of which hosts this blog) and a spare HDMI
cable. It struck me that surely there was some way I could set up the 
Raspberry Pi to play my videos for me. After some reading I discovered
that the [VLC Media Player](http://www.videolan.org/vlc/index.html) can
be controlled via a Telnet interface. For those of you who are not as
tech-savvy, Telnet is an old piece of software that can be used to 
remotely log onto computers in the command line. It long ago fell out of
favour due to security issues and has been replaced by software called 
SSH. However, as
I will only be accessing the Pi over my local network, security isn't much
of an issue and Telnet will be fine.

Now, I could simply log into VLC over Telnet and control it via the 
command line. This actually wouldn't be so bad, but I felt like there were
nicer, tidier alternatives. So instead I set to work writing a program
in [Python](http://www.python.org/) which could provide a graphical user
interface (GUI) for the Telnet controls. This was actually quite a new
experience for me, as almost all of my previous programming experience
has been in writing little scripts to process data and which have, at
most, a command line interface (although more often than not I just 
program my specifications directly into the code itself--so-called 
"hard-coding"). What little experience I have with GUIs has all been
for Windows, using a framework not available on Linux. So I had to 
learn how to work with a set of software libraries called GTK+ 3. 
[GTK+](http://www.gtk.org/) is
one of the two major frameworks used to design GUIs on Linux, the other
being [QT](http://qt-project.org/).

One thing that was nice is that there is a piece of software out there
called [Glade](https://glade.gnome.org/) which allows you to design GTK
interfaces visually and
then import them into your code (rather than have to create the whole
interface using code only). It's a bit rough around the edges, but 
certainly better than having to create the interface manually.

<a name="software"></a>

![Conetroller interface](|filename|/images/ConetrollerInterface.png)

And so, I now have a working piece of software that will allow you to
control a remote instance of VLC. So far I have only been able to test
it on an instance running on my own computer, but I see no reason why it
would work any differently if VLC is on a different machine. And thus,
I present to you: Conetroller v0.2.*

I am posting the code [for download here](|filename|/attachments/conetroller-0-2.tar.gz)
, if anyone is interested. 
Currently it is only able to run on Linux (there's a good chance it
would work on Mac OSX too), although it shouldn't be too difficult to 
port it to Windows, if you want to. It can be installed by executing
the following in a terminal:

    :::shell-session
    wget redshadesofgreen.raspctl.com/attachments/conetroller-0-2.tar.gz
    tar -zxvf conetroller-0-2.tar.gz
    cd v0.2/
    sudo ./install.sh
    

This installation technique is known to work in Linux Mint Debian 
Edition, and has not been tested anywhere else. However, I didn't do anything too exotic
in terms of directory layout, so it should work with most Linux distributions,
and certainly most Debian-based distros (eg: Ubuntu). Make sure to take
a look at the README file. No other documentation is
provided, but the interface is pretty simple and you should be able to
figure it out. If you have any question or problems, post them in the 
comments section below.

Current features include:

* Adding items to the playlist (using a URL or filepath)
* Clearing the playlist of items
* Play, pause, stop, skip forwards, and skip backwards buttons
* Displaying items currently on playlist
* Ability to scroll through video
* Recalling the most recent VLC instance logged into at the beginning of 
each session

Bugs, missing features, and other short-comings:

* No indication is given as to which playlist item is currently being 
played (it is unclear if this can be added while using the Telnet
interface)
* No ability to select an item from the playlist (likely will be added
in future versions)
* No ability to remember passwords (it would be insecure to store these
unencrypted in a plain text file, as was done with other login 
information). Future versions may include integration with Gnome Keyring
to overcome this.
* No comments included in the source code--I'll fix this sooner or later,
although I think it should be fairly easy to follow even without them
* Possible overuse of global variables in the code, rather than passing
them to the relevant functions--this may be fixed in future, although
I blame some of the peculiarities of Glade for this

Flaws aside, I am confident that Conetroller will prove useful to me,
and hope it can be useful to others as well.

*For those that are unaware, the logo for VLC is a traffic cone. Since my
program controls VLC, Conetroller seemed like the only reasonable name for it.
