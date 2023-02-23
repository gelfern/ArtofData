---
layout: post
title: The American View on Abortion (1975-2022)
subtitle: Preparing a dataset for analysis
thumbnail-img: /assets/img/ByBodyMyChoice.jpg
cover-img: /assets/img/preRoe.jpg
tags: [Lab]
comments: true
---
# “Choice” is dignity. 
# Moreover, “choice” is freedom. 

### Introduction
I simply cannot resist a brief history lesson -- the story of Roe v. Wade fascinates me:  
Jane Roe, born “Norma McCorvey" in 1947, lived in Texas under the custody of a single alcoholic mother. McCorvey was already married and pregnant by the time she reached my age; I still have trouble flipping eggs on a frying pan without breaking them in half. Facing a cold, harsh reality of harboring a life within her, only halfway through her teenage years after being raised in an insecure household, McCorvey had no choice but to carry a pregnancy to term before giving her own child away to her mother. 

Pregnant again in 1969, McCorvey wanted an abortion, which was inaccessible to her **unless** her life became threatened by the pregnancy. Subsequently, McCorvey was referred to feminist lawyers, Linda Coffee and Sarah Weddington, who were searching for a client to challenge abortion laws. By the time Coffee and Weddington changed Roe's case (McCorvey anonymized her name to Jane Roe) to a class-action lawsuit and a federal judge panel ruled that Texas’s abortion laws were unconstitutional, Mccorvey had given birth and gave this child up for adoption. However, when the state of Texas appealed, the Supreme Court ruled that women had the right to an abortion during the first trimester of pregnancy, “free of interference by the state,” in 1973. Thus, _Roe v. Wade_ was born. 

It is at this point (1973) in history that the [dataset](https://www.kaggle.com/datasets/justin2028/perspectives-on-abortion-1975-2022) I am extrapolating from becomes relevant, which "describes the **changing perspectives** on a woman's right to **choose** in America." 
As explained by [Justin Oh](https://www.kaggle.com/justin2028), who put together this dataset and posted it on [Kaggle](https://www.kaggle.com/), all official figures are from Gallup, a global analytics firm which is formerly known as the American Institute of Public Opinion. [Gallup](https://www.gallup.com/home.aspx) is uniquely equipped to properly illustrate how the American opinion on abortions has shifted between just after _Roe v. Wade_ and just before the _Dobbs v. Jackson Women's Health Organization_ ruling in June 2022, which effectively overturned the national precedent on abortion set by _Roe v. Wade_. 

![FURY](../assets/img/fury.jpg)


To begin my exploration of America's shifting views on abortion, I analyzed the dataset corresponding to Question 1: **Should Abortions Be Legal?** 
This data contains responses to the poll from dates ranging from April 1975 (2 years after _Roe v. Wade_ was ruled) to May 2022 (the month before _Roe v. Wade_ was effectively overturned). 

Effectively, I begin this project with a "birds-eye view" of the general American sentiment regarding the legality of abortion during the period of time where _Roe v. Wade_ was in-effect. It is critical to note that the dataset corresponding to question 1 is based on the responses of registered votes -- to me, this most obviously implicates two things: 

First of all, in 2020, about [62.8%](https://www.pewresearch.org/fact-tank/2022/11/01/turnout-in-u-s-has-soared-in-recent-elections-but-by-some-measures-still-trails-that-of-many-other-countries/) of Americans of voting age voted in the _presidential_ election, showing that 40 percent of Americans either are not registered to vote, or do not regularly civically engage. For this reason, as I conduct my analysis on the responses to the poll in question one I am keeping in mind the fact that the poll responses cannot verifiably describe the true opinions of the American public, but still can provide a valuable generalization. 

Second, as both biological men and women can vote, the opinions of both biological men and women are included in the poll I am analyzing. However, as I am a firm believer in the fact that the choice to have an abortion must only involve the desires of the woman who is considering having one, and, moreover, that abortion is not at all a political issue, but one of basic women's health, I acknowledge that the question posed by this poll is one I inherently have problems with because it automatically frames abortion as a legal issue to be decided by the men (and women) in government. Still, I am very interested in extrapolating from this data to provide myself with a more objective understanding of America's views on abortion, in place of the heavily biased information I consume through the media. 

The program below utilizes the pandas .describe() function to calculate the mean, minimum value, and maximum value of the percentages of people affiliated with each category of the poll. 

![FURY](../assets/img/CodeDescribe.jpg)

![FURY](../assets/img/describe.jpg)

To me, one of the most interesting pieces of data from this calculation is the mean percentage of Americans who believe that abortion should be legal only under certain circumstances (ie. during the first trimester of pregnancy, as established by _Roe v. Wade_), which equals about 53%. In my personal experience, abortion feels like a heavily polarized issue, with people either agressively arguing its immoraility and describing it as murder, or people expressing that they feel entirely unentitled to even have a personal opinion on the issue, effectively leaving abortion in the hands of women who choose to have one. Still, during the period of time when the _Roe v. Wade_ decision remained effective in America, about half of Americans shared a sentiment that reflected the Supreme Court's decision. Moreover, the maxiumum percent of Americans believing that abortion should be entirely illegal (even in the cases of sexual abuse or incest) reached 23%, with a minumum value of 12% over the course of 1975 through 2022. While I find that any amount of people that feel entitled to claim that abortion should be illigal in every circumstance is alarming, the amount of Americans that feel this way has never exceeded 2/5 of the country. Therefore, I am compelled to ask why [12 states](https://www.guttmacher.org/2023/01/six-months-post-roe-24-us-states-have-banned-abortion-or-are-likely-do-so-roundup) -- about 25 percent of the country -- have essentially total abortion bans in effect, when not more than 23% of American voters have ever felt that abortions should be entirely illegal. Also, as about [58%](https://www.guttmacher.org/united-states/abortion?gclid=Cj0KCQiAutyfBhCMARIsAMgcRJTMC4JZM1W2Oybb3jYIoQPQ9CX1VyTjbG4049Ydp-TdSEUFOFFaqtUaApDGEALw_wcB) of women ages 13-44 live in a state hostile or extremely hostile to abortion rights, I wonder how the (mean) 18% of Americans (both biological men and women) have their minority sentiment as the law in effect within 12 states, threatening over half of America’s female population. 


Next, I created a copy of the dataset containing the responses to **Question 1** to only include data on the years included on the x-axis of the layered bar chart below. 

Why the specific [dates](https://www.plannedparenthoodaction.org/issues/abortion/abortion-central-history-reproductive-health-care-america/historical-abortion-law-timeline-1850-today)?
* 1975: Two years after _Roe v. Wade_ and also the earliest year during which the datasets I'm using have poll responses 
* 1985: One year after the **Global Gag Rule**, (the dataset did not have poll responses from 1984) introduced by Ronald Reagan in Mexico City. This Mexico City Policy prevented foreign organizations that receive U.S. health aid from providing information on and referrals for abortions or advocating for abortion access, which has since been repeadedly rescinded and reinstated depending on the U.S. president in power. 
* 1992: _Planned Parenthood of Southeastern Pennsylvania v. Casey_, which reaffirmed that the U.S. Constitution protects the right to an abortion. This case created an "undue burden" framework, under which laws restricting access to abortion could be judged, leading to state politicians passing numerous medically unnecessary abortion restrictions across the country which courts have found do not impose an undue burden. 
* 2007: _Gonzales v. Carhart and Gonzales v. Planned Parenthood Federation of America_, where the Supreme Court upheld the first federal legislation to criminalize abortion, which allowed Congress to ban certain second-trimester abortion procedures (which are sometimes the safest and best way to protect a patient’s health). This case overruled a critical component of _Roe v. Wade_, which has expressed the importance of a patient’s health in laws that restrict abortion access.
* 2016: _Whole Woman's Health v. Hellerstedt_, where the Supreme Court ruled that two Texas abortion restrictions were unconstitutional because they would shut down most abortion providers in the state and impose an "undue burden" on safe abortion access in the state. 
* 2020: _June Medical Services v. Russo_, where the Supreme Court struck down a medically unnecessary law restricting abortions. 
* 2022: _Dobbs v. Jackson Women's Health Organization_, where the Supreme Court effectively overturned _Roe v. Wade_ and decided that the U.S. Constitution does not confer a right to abortion. 


Below is the code I wrote to generate the stacked bar chart as well as the graph, itself. 
![legalcode](../assets/img/CodeLegal.jpg)

![legal](../assets/img/legalfinal.jpg)


Next, I decided to assess Americans' views on if abortion was morally wrong, and to visualize how this number has changed, specifically between 2007 (_Gonzales v. Carhart and Gonzales v. Planned Parenthood Federation of America_), 2016 (_Whole Woman's Health v. Hellerstedt_), and 2022 (the month before _Dobbs v. Jackson Women's Health Organization_). 

![FURY](../assets/img/CodeMorals.jpg)

![Morals](../assets/img/MorallyAcceptable.jpg)

My main takeaway from this bar chart is that between 2007 (when the Supreme Court first upheld legislation to criminalize abortion) and 2020 (when the Supreme Court decided that the U.S. Constitution does not protect the right to an abortion), the American public's view that abortions are morally wrong visibly declined. It is interesting to see how while Americans see abortion as less and less of a moral issue, the U.S. federal government has relinquished its authority to protect its legality and several state governments have taken it upon themselves to enforce near total bans on abortions. 



At this point, I became interested in not only the American sentiment on the deserved legality and morality of abortion, but also how we (as citizens entitled and encouraged to engage civically) express our satisfaction with and opinions on abortion laws in our country. 

Therefore, I first visualized the responses to the question **Are you Satisfied or Dissatisfied with American Abortion Policies**, during 5 critical years to the reproductive rights movement. Importantly, included 2001 because it was the earliest year for which my dataset contained poll responses. For the other 4 years that I displayed the distribution of poll responses for, I specifically chose them for the same reasons as I explained for the graph, "Should Abortions be Legal?". 

The code I wrote to generate the stacked bar chart:
![satisfied](../assets/img/CodeSatisfied.jpg)

![Satisfied](../assets/img/Satisfied.jpg)

What stands out to me most from this graph is the fact that the amount of Americans who were very satisfied with the nation's abortion policies visibly declined, while the section of the bar chart corresponding to "very dissatisfied" visibly grew. Keeping in mind that the datasets I am using can only provide generalizations of American perspectives on abortion, I still feel confident to conclude that Americans are growing less and less satisfied with how our nation treats abortion rights. 
Moreover, between 2007 (when the Supreme Court upheld the first federal legislation to criminalize abortion) and 2022 (right before _Roe v. Wade_ was overturned, but after the case was leaked to the American public), the bright pink box corresponding to "very satisfied" continuously shrunk, to over less than half its original size. I find that using seaborn to generate this bar chart was extremely useful to visualize a correlation between the U.S. government increasingly intervening in a woman's right to choose and the nation's approval of our legislative bodies doing so declining. 
Specifically, while I, in doing this project, cannot prove a causal relationship between these two factors (abortion legislation and a citizen's approval/satisfaction), I am extremely interested in further exploring this correlational relationship and diving deeper into the nuances of state-by-state abortion legislation, and the sentiments of the American public during the 20th century. 


Because I observed a correlation between the U.S. government passing more restrictions on abortion and the public's diminishing satisfaction with the nation's rapidly changing policies, I began thinking about the main way that we, the people, can express our power over our government -- voting. Therefore, I separated one dataset into two graphs that described how a political candidate's position on abortion would affect/affects an American citizen's vote. The first graph displays data for this question for American adults (whether or not they are registered voters) and the second graph displays data for this question only for registered voters. 
Effectively, if such a small "chunk" of our country is satisfied with how America is handling the legality of abortion, I was interested to see how this translates into importance of abortion as a legal issue, especially if potential candiates would pose threats to abortion rights. 

![adultscode](../assets/img/nationaladults.jpg)

![Adultsgraph](../assets/img/nationaladultsgraph.jpg)


![FURY](../assets/img/CodeRegistered.jpg)

![Voters](../assets/img/Voters.jpg)

In reflection, between the years of 1996 (the earliest year for which my dataset had poll responses) and 2022, the importance of a political candidate's view on abortion visibly grew for all national adults -- registered or not --(the bright pink section of the layered bar charts), in tandem with the U.S. government enforcing more restrictions on abortions and the American public growing less satisfied with the nation's policies on abortion. 

My hope for the future, after visualizing the changes in how American citizens value political candidates' positions on abortion (especially after seeing that the graphs for all adults and just registered voters look quite similar), is that not only will more adults register to vote, but that more adults will perceive abortion as under and existential threat. The future of women's reproductive health is truly in the hands of the American public. 

### Limitations
Though I have already discussed some existing with the datasets I have used to complete this lab, I think that the largest limitation is that while Gallup is an acclaimed and verifiable accurate source of global analytics data, it is currently unclear to me exactly how the data I used was collected, and how I can be sure that as many sources of bias as possible have been dealt with. Therefore, I have completed this lab under the assumption that the data I am visualizing is not completely accurate, but can provide an accurate generalization of the American sentiment on a variety of questions.  



Please note that sections of my introduction have been taken from a larger research article I have been writing for the Folio 51 magazine on Reproductive Rights. 

Historical References: 
Bauer, Pat. "Norma McCorvey." Encyclopedia Britannica, 23 Jan. 2023, https://www.britannica.com/biography/Norma-McCorvey.

Britannica, The Editors of Encyclopaedia. "Roe v. Wade." Encyclopedia Britannica, 24 Aug. 2022, https://www.britannica.com/event/Roe-v-Wade.

Image References: 

[Thumbnail](https://www.nbcbayarea.com/news/national-international/photos-protests-erupt-across-the-nation-after-supreme-court-leak-of-roe-v-wade-draft-overturning-abortion-rights/2881065/)

[Cover](https://www.theatlantic.com/ideas/archive/2020/03/before-roe-v-wade/607609/)

[American Women Scorned](https://www.voanews.com/a/us-prepares-for-post-roe-v-wade-future/6632410.html) 

