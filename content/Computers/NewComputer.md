Title: New Computer, New Linux Distribution
Date: 2013-07-30 15:00
Tags: Linux, Arch Linux, Laptop, MATE Desktop
Summary: My old laptop was dying and I wanted to replace it before the semester began. The new laptop came with Windows 8 installed and I was not having that, so the choice now became what version of Linux to use. The obvious choice would have been Linux Mint, which I have used ever since moving to Linux. But another Linux distribution which I'd heard interesting things about is called Arch Linux.

Well, my old laptop was dying. At least I think it was. In any case,
I wasn't waiting around until the semester started to find out--better
to get a new computer now when I had time to get it configured properly.
And so, a week and a half ago I found myself with a brand new ASUS laptop.
It's not actually an ultrabook but it is still pretty thin. It has a 24GB
solid-state drive (more than enough to hold my operating system), a 750GB
mechanical hard drive, an Intel i5 processor, an optical disc drive,
and a 14\" screen. Overall I'm quite happy with my choice.

The laptop came with Windows 8 installed. I was not having that. The 
choice now became what version of Linux to use. The obvious choice 
would have been [Linux Mint](http://www.linuxmint.com/), which I have 
used ever since moving to Linux. This distribution has the advantage of
being ready to use immediately after installation. I'm also very 
impressed by their [Cinnamon Desktop Environment](cinnamon.linuxmint.com).
However, the trade-off in a distribution being easy to use is that it
also somewhat inefficient when it comes to hardware usage. 
Additionally, in order to upgrade Linux Mint you must totally re-install
the operating system. To put it lightly, this is a frig.

Another Linux distribution which I'd heard interesting things about is
called [Arch Linux](https://www.archlinux.org/). In a sense, Arch is the
polar opposite of Linux Mint. Once you've installed it, you have a 
command-line interface with a basic software set installed. And that's
it. Everything else, including device drivers and a graphical interface,
you must install yourself. However, this ensures that there will be 
absolutely no bloat on your computer. Arch Linux also has the advantage
that you never have to install a new version of the operating system: all
of the components can be upgraded in exactly the same way that you'd upgrade
any other software. (For those who are familiar with Linux, this means 
that you just keep the OS up-to-date by applying the upgrade command
with the package-manager.) 

For some reason I decided that I wanted to give Arch a try. A big part
of the appeal is not having to re-install the OS for upgrades. I was also
enticed by the amount of control I'd be able to have over my system. And
I guess at the end of the day I wanted the challenge--I enjoy tinkering
with my computer, and I'd reached the limits of what I could do with Mint.
In other words, I chose it out of masochism. 

The installation process is considerably more complicated than that for
Linux Mint. However, in principle it isn't too difficult, thanks to the
wonderful documentation provided. Unfortunately, my computer has one of
those awful new UEFI motherboards. This, combined with some feature
called "secure boot" meant that even getting my computer to detect the
installation disc was a struggle. Then, once I finally got Arch installed,
the UEFI boot-loader was convinced that there was no operating system
present. To be fair, I tried installing Linux Mint and encountered the
same problem. Several attempts later, I finally found a work-around that
got the boot-loader to see the operating systems.

![Bow to me, for I am root](|filename|/images/iamroot.jpg) At this point I 
was past the worst. The next step was to create a new
account for myself. Initially when you install Linux (well, in more
traditional setups like Arch, anyway) there will only be one user, called
"root." Root is capable of doing anything on the computer--it can delete
or edit any file. This is actually quite dangerous (giving rise to the
expressions "He who plays with root kills \[file-\]tree") as you can
potentially delete something vital for the operation of your computer.
Thus it is best to create a separate account for every-day work
on the computer and only to use root when necessary (such as when installing
new software). Speaking of installing software, that was the next step.
First were the drivers for things like sound, video,
and my laptop's trackpad. Next came a graphical user interface (GUI).
Linux uses the X Window System for this. However, all that X gives is the
ability for the computer to render graphical windows--you can't do very
much with them by default, and you certainly won't have a desktop with icons.
For that I needed to install a Desktop Environment.

My first choice for a desktop environment was Cinnamon. It has a fairly
traditional layout (which I like--I don't know why so many projects are
trying to force totally new interfaces on people) but modern looking
visual features. Unfortunately, Cinnamon's behaviour with Arch was
distinctly underwhelming. There were numerous problems, but probably
the most frustrating was that I couldn't get any of the applets (such as
the one which shows the weather) to work. Additionally, I realized how
tricky it can be to configure some of the visual elements of Cinnamon. On
Linux Mint this isn't really a problem because most of the work is done 
for you in advance, but I couldn't seem to get it looking quite the way I wanted on
Arch. So I gave up on Cinnamon.

My second choice was [MATE](http://mate-desktop.org/).
MATE is a fork of an older desktop environment (now discontinued) called
GNOME 2. MATE was created when GNOME 2 was replaced by the horrendous 
GNOME 3. MATE doesn't (by default) have quite the same level of prettiness
as Cinnamon, but on the other hand it is far easier to configure. So I
installed MATE and almost immediately realized that I could get rid of 
Cinnamon: all of MATE's features worked immediately. So goodbye Cinnamon.
After installing a few more themes, MATE looked almost as good as 
Cinnamon, too!

Finally I needed to install my preferred applications. It was the usual
sort of list: [LibreOffice](http://www.libreoffice.org/), 
[emacs](http://www.gnu.org/software/emacs/), [Banshee](http://banshee.fm/), 
[Geany](http://www.geany.org/), and [Texmaker](http://www.xm1math.net/texmaker/).
Perhaps my favourite feature of Arch Linux is the Arch User Repository.
This is a collection of source-code for software which would not be
popular enough (or is still too experimental) to warrant being maintained
in the official software repositories. However, Arch users can prepare
the source code themselves so that it can easily be compiled into a package
and then installed using the normal package manager. This means that there
are some obscure, but great, pieces of software which can be installed
with ease, such as a client for my [Seafile](http://www.seafile.com/en/home/)
Cloud Server (an open source replacement for Dropbox) and 
[Pelican](http://docs.getpelican.com/en/3.2/), which I use to produce 
this blog. 


<img style="float:none;display:block;margin-left:auto;margin-right:auto" alt="A screenshot of my desktop." src="http://redshadesofgreen.raspctl.com/static/images/ArchScreenshot.png" />


And this brings me more-or-less to where I am now. While there are still
a few things I have left to do, at this point I have a fully functional
computer running Arch Linux.
