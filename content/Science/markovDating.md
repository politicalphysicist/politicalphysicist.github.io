Title: Markov Chains and Gay Dating
Date: 2013-07-02 13:30
Tags: Dating, Markov Chains, Mathematics, Mathematical Models
Summary: When you're gay and want a serious relationship, you have to deal with the fact that a lot of guys out there just want casual sex. Some days it feels like I must be the only gay guy in the city who actually wants commitment. However, it has been pointed out to me that because those who want serious relationships will tend to find each other and drop out of the dating pool, it will appear that a much greater portion of gay men want only casual sex than is actually the case. Digging out my old Linear Algebra textbook, I realized that there exists a useful tool to analyze this trend: Markov Chains.

So, in case you didn't realize, dating when you're gay is *hard*. Not to say 
it's easy for straight people, but at least you know that, when you talk to
someone, the odds are that they at least have a compatible sexuality. Not to mention that  
when you're gay and want something serious you have to deal with the fact that
a lot of guys out there just want casual sex. This, it seems, is especially true
online and in gay bars. Some days it feels like I must be the only
gay guy in the city who actually wants a committed, monogamous relationship.

At some point, however it was pointed out to me that part of the reason it can
feel that way is because those who want serious (read, monogamous) 
relationships will tend to find each
other and drop out of the dating pool--at least temporarily. Or, given my 
science background, I prefer to think back to my high school chemistry classes
and say that they precipitate out of the solution. (Actually, given the effect 
that this has on the reaction's rate and equilibrium, this might be a surprisingly
apt analogy.) Thus it will
seems as though there are artificially few gay men seeking what I want. Of 
course, being someone who likes things to be quantitative, I wasn't entirely 
satisfied with such a qualitative explanation. I found myself wondering how
dramatic was this affect and just how much it could bias what I see.

Luckily, I remembered some concepts from my linear algebra classes that I thought
would be useful in evaluating these questions. Taking out my old textbook, I
quickly found that what I wanted are called Markov Chains. To quote the
[Wikipedia article](https://en.wikipedia.org/wiki/Markov_chain), a Markov Chain
is:

> . . . a mathematical system that undergoes transitions from one state to 
> another, between a finite or countable number of possible states. It is a 
> random process usually characterized as memoryless: the next state depends 
> only on the current state and not on the sequence of events that preceded it.

For the purposes of this post, we will assume that there are only threes
states for gay males:

1. Interested in hookups (A)
2. Interested in a serious relationship (B)
3. In a serious relationship (C)

This is obviously a gross oversimplification. In the future I may well add more
categories. There are various other problems which will become apparent as we
work through this simple analysis; I will point them out as we get to them.

Now, Markov Chains can be represented by graphics such as the one below:
![There are three circles, representing the three groups, with paths connecting them. On each path is a probability of someone following that path between time steps.](|filename|/images/markovDating.png)

The label $P_{XY}$ next to each of the arrows is the probability that a member
of group X will move to group Y over some time-period--say, one month. These 
probabilities can be represented by the following matrix: 
$$P = \begin{bmatrix} 
P_{AA} & P_{BA} & P_{CA} \\\\\\\\
P_{AB} & P_{BB} & P_{CB} \\\\\\\\
P_{AC} & P_{BC} & P_{CC} 
\end{bmatrix} .$$

If you have some population of gay men then you can represent the number of men
in each group as a vector 
$$\vec{N_0} = \left( \begin{array}{c} A_0 \\\\\\\\ B_0 \\\\\\\\ C_0 \end{array} \right).$$
The number of people in each group after one month would then be given by
$$\vec{N_1} = P \vec{N_0}.$$ More generally, $$\vec{N_{n+1}} = P \vec{N_n}$$ 
implying that $$\vec{N_k} = P^{k} \vec{N_0}.$$ One of the properties of the 
matrix representations of Markov Chains is that $$\lim_{k \to \infty} P^{k}$$ 
converges to some matrix $L$ which represents the system's equilibrium state. The
columns of the matrix will all be the same vector, $\vec{x}$, known as the
steady-state probability vector. This represents the fraction of people
in each group once the system has reached its steady-state. It follows that
the system will eventually reach this configuration no matter what the
starting conditions.

So now we've set up a simple model of the gay dating scene. But, before I 
continue, I need to highlight a weakness of this model; it doesn't (explicitly) 
account for age-groups. It can not  account for people's attitudes changing as t
hey mature or for the entrance of new, younger
people into the dating pool. This has an impact on what values we choose when
filling our matrix. For example, my suspicion is that many guys who are 
initially into hookups will, after having had their fun and with some increased
maturity, become tired of 
them and want a more serious relationship. However, in the real world, this
may be offset by new people entering the dating pool. None of this can be directly
modelled here, which is a weakness of these simple
Markov Chains. If I decide to continue this sort of analysis in future, it
would suggest that I should abandon them in favour of a more complex model. 
For the purposes of *this* article, let's just assume that the
people in the dating pool don't mature or alter their attitudes. This is
almost certainly wrong, but it would require a far more complicated model, in
which the various probabilities depended not only on someone's current 
relationship status but also on their relationship history, to overcome this 
limitation.

Given these simplifications, let's see what assumptions we can reasonably make 
about the value of our $P$ matrix:

1. Someone who seeks hookups will not start looking for a relationship. 
($P_{AB} = 0$)
2. Occasionally a hookup will turn into a relationship. ($P_{AC} > 0$)
3. Someone who wants a relationship will not change to wanting hookups. 
($P_{BA} = 0$)
3. Relationship generally last more than one iteration of the model. 
($P_{CC} > 0$)
3. When a someone gets out of a relationship they will seek another relationship
and not hookups. ($P_{CA} = 0$)

The last assumption is the one which strikes me as the most inaccurate, as 
someone who entered a relationship via a hookup would probably go back to 
hookups and someone who gets out of a long-term relationship might want to 
partake in hookups for a little while before looking for a new relationship.
However, to properly account for these things would require me to know the
history of the system, which would mean I could no longer use a simple Markov 
Chain. 

We can now start filling in the matrix:
$$P = \begin{bmatrix} 
1 - P_{AC} & 0 & 0 \\\\\\\\
0 & 1 - P_{BC} & 1 - P_{CC} \\\\\\\\
P_{AC} & P_{BC} & P_{CC} 
\end{bmatrix} .$$

Let's say that each iteration of the model corresponds to one month. 
Furthermore, let's assume that someone seeking hookups has an ~1% chance of 
ending up in a relationship over the course of a year, or a 0.1% chance of ending
up in a relationship each month. We'll assume that the probability of a 
relationship lasting one year is ~50%, ie: there is a 94% chance they will last
each month. These are numbers which I essentially made up, but they seem
reasonable to me. Unfortunately, I have no idea what the odds are of someone 
entering a relationship each month. I'll just guess and say 5% (which 
corresponds to an ~45% probability of entering a relationship over the course
of a year). Thus: 
$$P = \begin{bmatrix} 
.999 & 0 & 0 \\\\\\\\
0 & .95 & .06 \\\\\\\\
.001 & .05 & .94 
\end{bmatrix} .$$

Using the [GNU Octave](http://www.gnu.org/software/octave/) software (an open
source clone of MATLAB), I computed  $P^{k}$ using larger and larger values
of $k$ until the results converged on some matrix $L$, as described above. This
didn't happen until $k \approx 13000$. That is to say, it took this system
1083 years to reach equilibrium. I think it is safe to say that my assumption
of people in the model not maturing as I iterate the model
is pretty invalid! For those that are curious, the steady-state probability
vector is 
$$\vec{x} = \left( \begin{array}{c}0 \\\\\\\\
0.55 \\\\\\\\
0.45\end{array} \right).$$

A more meaningful thing to do would be to look at how the number of people in
each group changes over time. In my current city there are probably around 
30,000 post-secondary students during the school year. Assuming that half of
them are male and that 5% of males are gay, that works out to 750 young gay
men. We'll assume that initially none of them are in a relationship, that half
of them are interested in hookups, and that half of them want a relationship.
The number of people in each relationship is shown in the graph below over a
period of four years.

![Group A appears to decrease more or less linearly in size, Group B decreases rapidly at first and then levels off, and Group C increases quickly at first before levelling off.](|filename|/images/markovRes.png) At the end of the four year period, there are 357 people looking for hookups, 
213 peoples looking for a relationship, and 180 people in a relationship. Even
though half of the population (and increasing) is long-term-relationship 
oriented, these people make up only 37% of the dating pool. I'd be very 
interested to know how closely this corresponds to reality. Of course, 
evaluating reality
is made more complicated by things like open relationships and people who are
seeking a relationship but will partake in hookups in the meantime. 

Finally, according to this model, it turns out that those seeking a relationship
will, four years in, be in a minority within the dating pool so long as initially
more than 37% of people are interested in hookups. So this
tends to indicate what I suspected--even though it might feel like you're alone in
seeking a long-term gay relationship, there is a good chance that the majority
of gay guys actually share your views. Now the only problem is finding them!
