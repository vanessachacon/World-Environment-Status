# Title: Global Environmental Issues Today 

## Overview: 

The aim of this web application is to quickly access information regarding environmental issues around the world. Currently while there is an abundance of information on environmental issues, there is no quick way to look up by country what those issues are or to identify which environmental hurdles any one country is specifically facing. 

## Features (User stories):

>As a **citizen**, I want to **sort** what environmental issues my country is currently facing so I can be prepared and/or educated.

>   

>As a **business**, I want my know what environmental issues we are facing or might face in new markets **by tracking where certain issues are currently taking place.** This might help us avoid costs.
>

>As an **environmentalist**, I want to **identify** regional trends. If everybody is up to date on what those shared issues are, consensus can be built to reach solutions to whatever environmental challenge there might be.
> 

>As a **business**, I want to **identify where my business might be of help** (ie Ridwell)  
  



### Tasks:
1. need to add search bar/feature to search by country or issue. A drop down lists for each might be helpful.

2. generate appropriate info based on search query.

3. keep tabs on which environmental issues users have the most concern about at any given time. (need to store data somewhere)

4. generate chart of searches(organize date and display)

6. page layout; title, search bar, links,  generate chart of most asked about items or image slide with chart, environmental inspiration/education news, etc. Linked sites, appropriate info per link.  


## Schema (Data Model):

>Country  
    -environmental issues
>
>Environmental issue 
    -countries currently dealing with certain environmental issues
   
>
>Count 
    -Most searched item  
    -largest environmental issues (by number of countries)
    -countries with largest environmental issues (subjective)
>


## Shedule:
### Week 1:
1. Capstone Proposal
2. Repo 
3. Create Django Project
4. Create Models
5. finding appropriate api/data
6. setting storage of data. 
7. Search capablity (by text)
8. sorting feature of data into countries vs environmental issues
9. images on each corresponding page with text/name of country/environmental issue in question
10. basic layout/css

### Week 2:
1. workout kinks/make sure its MVP
2. keep tabs on searches (django? sql? )
3. Generate chart of searches (the chart i used in first capstone/forgot name)
4. nice css on normal browser

### Week 3:
1. add environmental inspo/education/news(nyt api/npr api/ possibility?)
2. add image slide on homepage of count data/graphs
3. seemless css in all kinds of devices


## Must/Should/Can/ Won't Haves

### Essential features:
- Search capablity (by text) by country or environmental issue
- Images on each corresponding page with text/name of item in question
- basic layout/css

### Really-great-to-haves:
- Keep tabs on searches
- Generate chart of searches
- Nice css on normal browser

### Nice-to-haves:
- Environmental inspo/education (api to nyt or npr for news)
- Image slide on homepage(bootsrap) for chart
- Seemless css in all kinds of devices
- Search by image on browser or map (advanced)
- Info regarding North American continent

### won't have:

- environmental laws/ deals/treaties info
- info regarding all countries. 
