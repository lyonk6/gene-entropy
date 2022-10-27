# gene-entropy

We seek to quantify the complexity of a sequence of DNA or RNA. To do this we use two aproaches. First we will first calculate the entropy of a gene, then we will attempt to calculate it's [assembly index](https://www.nature.com/articles/s41467-021-23258-x). 

## Information
An event that is guaranteed to happen gives no information while an event that occurs with a known probabilty of $1/n$ gives $n/2$ bits of information. More generally, we can express information in other units by changing the devisor. That is, if we choose to use a different unit than bits we can simply divide n by a different number. For example, we could say that a RNA sequence of length 3 gives 3 bases of information if we define a 'base' as existing in exactly 4 states:

$$ P(base) = 1/4 $$
$$number\: of\: bases = 3 $$


$$ 3  \times 1/4 = 3\:Bases $$

## Entropy
If _information_ tells use what a given outcome is, then _entropy_ tells us about the outcomes we didn't observe. Entropy is a measure of uncertainty or randomness in a system. The Shannon entropy $H(x)$ of some information is given by: 
$$-\sum_{i=1}^n P(x_i) log P(x_i) = H(x)$$

So the Shannon entropy of a RNA molecule "agc" is:

$$H(x) = -[P(a) log{_2} P(a) + P(g) log{_2} P(g) + P(c) log{_2} P(c)]$$


$$ = -[(^1/_4) log{_2} (^1/_4) + (^1/_4) log{_2} (^1/_4) + (^1/_4) log{_2} (^1/_4)]$$


$$ = -(^1/_4) [log{_2} (^1/_4) + log{_2} (^1/_4) + log{_2} (^1/_4)]$$

$$ = -(^1/_4) ([-2] + [-2] + [-2])$$

$$ = (^6/_4)$$

$$H(x) = 1.5 \: bits$$ 

## Assembly Index

Given that all genes are defined by a sequence of 4 distinct molecules, what is the smallest number of operations to create a given gene with the following operations: 

1. A gene starts with a single letter which can be any of {a, c, g, u}. 
2. A letter be added on either the start of a string or to the end.
3. Any subseqence of a gene can be similarly added to either the start of said gene or to the end.
