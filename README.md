# gene-entropy

We seek to quantify the complexity of a sequence of DNA or RNA. To do this we use two aproaches. First we will first calculate the entropy of a gene, then we will attempt to calculate it's [assembly index](https://www.nature.com/articles/s41467-021-23258-x). 

## Information
An event that is guaranteed to happen gives no information while an event that occurs with a known probabilty of 1/n gives n/2 bits of information. If we choose to use a different unit than bits we can simply divide n by a different number. For example, we could say that a RNA sequence of length 3 gives 3 bases of information if we define a 'base' as existing in exactly 4 states. 

## Entropy
The Shannon entropy $H(x)$ of information is given by: 
$$-\sum_{i=1}^n P(x_i) log P(x_i) = H(x)$$

So the Shannon entropy of a RNA molecule "agc" is:

$$H(x) = -[P(a) log{_2} P(a) + P(g) log{_2} P(g) + P(c) log{_2} P(c)]$$


$$ = -[(^1/_4) log{_2} () + (^1/_4) log{_2} (^1/_4) + (^1/_4) log{_2} (^1/_4)]$$


$$ = -(^1/_4) [log{_2} (^1/_4) + log{_2} (^1/_4) + log{_2} (^1/_4)]$$

$$ = -(^1/_4) ([-2] + [-2] + [-2])$$

$$ = (^6/_4)$$

$$H(x) = 1.5 \: bits$$ 

## Assembly Index

