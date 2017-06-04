# wikiquote_fortune

[![Build Status](https://travis-ci.org/Yailm/wikiquote_fortune.svg?branch=master)](https://travis-ci.org/Yailm/wikiquote_fortune)

Retrieve quotes from wikiquote.org and generate fortune cookie
inspired by the `python-wikiquote` and `wikiquote_fortune`

## Usage

$ python wikiquote_fortune.py "beauty and the beast"    # TV show name  
[1:Beauty and the Beast (2017 film)]  
    Beauty and the Beast is a 2017 American musical romantic fantasy film about a young intellectual girl named Belle, who is taken prisoner by a fearsome Beast in his enchanted castle and she learns to look beyond his appearance while evading a narcissistic hunter who seeks to take Belle for himself.

[2:Beauty and the Beast (1991 film)]  
    Beauty and the Beast is a 1991 film about a young, beautiful French girl who falls in love with a hideous beast.

[3:Beauty and the Beast (1987 TV series)]  
    Beauty and the Beast (1987-1990) was An Urban Fantasy series staring Linda Hamilton and Ron Perlman. After a brutal attack in central park ADA Catherine Chandler is brought into an underground society that lives in caves and tunnels deep under New York.

option (1..3, others for aborted):   
"beauty and the beast (2017 film).dat" created  
There were 62 strings  
Longest string: 3268 bytes  
Shortest string: 7 bytes  

Copy the generated files into `/usr/share/fortune`
