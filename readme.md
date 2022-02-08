# Title: Recycle Me!

## Project Overview: 

The aim of this web application is to practice proper recycling. Currently the app for Hillsboro waste recycling does not have a feature that tells citizens what is recylable and what is waste. This app wil help reduce, if not eliminate, "Wishful Recycling" which is where customer's wish items that are not recyclable become so. This is a problem because it impedes the ability of waste servicers to properly recycle items. 

## Features (User stories):

As a **citizen**, I want to **sort** what can and can't be recycled so I can seperate my trash correctly and responsibly. 
As a **customer**, I want to **know** what to do with non recyclable products so that I am not fined.
As a **business**, I want my customers to follow rules accordingly to maximize potential profits and cut down costs **by tracking what items customers are confused about.**
As an **environmentalist**, I want clean streets, water, and air. If everybody is **educated about "reduce, reuse, and recycle" our carbon footprint can be reduced.**
As a **business**, I want to **help customers dispose of items their waste disposal company cannot to help my company generate business** (ie Ridwell)
As a **customer**, I want a reliable way to **determine what to do with discarded items and alternatives if I can't recycle or dispose of items normally.** 
As a **city**, we want citizens to dipose of items properly to  minimize landfill waste by **providing adequate disposal services.**

### Tasks:
1. need to identify/filter which items are disposable, recyclable with corresponding to do lists (washed, lid thrown away, etc (possibly))

2. click on links for garbage, recycle, hazardous items, alternate forms of disposal/contact info/ hazardous disposal days (ie paints, solvets, etc)        donation sites (clothing scrapts/etc @places like dog shelters etc.)

3. keep tabs on which items users have the most confusion about (i.e. clamshells? lids? ) (need to store data somewhere)

4. generate chart of searches(organize date and display)

5. ability to search for item by name(text) (and/or by image-hopefully)

6. page layout; title, search bar, links,  generate chart of most asked about items or image slide with chart, hazardous disposal days, environmental inspiration/education news, etc. Linked sites, appropriate info per link.  


## Schema (Data Model):

Recyclable
    items
    count
Garbage
    items
    count
Hazardous
    items
    count
Other
    items
    count
Most searched item
    items
    count

items(separately ?)



## Shedule:
### Week 1:
1. Capstone Proposal
2. Repo 
3. Create Django Project
4. Create Models
5. finding appropriate api
6. setting storage of data. 
7. Search capablity (by text)
8. sorting feature of data into garbage, recyclable, etc
9. images on each corresponding page with text/name of item in question
10. white and green color layout/css

### Week 2:
1. workout kinks/make sure its MVP
2. keep tabs on searches (django? sql? )
3. Generate chart of searches (the chart i used in first capstone/forgot name)
4. search by image (flickr)
5. nice css on normal browser

### Week 3:
1. add environmental inspo/education
2. add image slide on homepage
3. add alternate forms of disposal links/info (ridwell api?)
4. seemless css in all kinds of devices


## Must/Should/Can/ Won't Haves

### Essential features:
- Search capablity (by text)
- Sorting feature of data into garbage, recyclable, etc
- Images on each corresponding page with text/name of item in question
- White and green color layout/css

### Really-great-to-haves:
- Keep tabs on searches
- Generate chart of searches
- Nice css on normal browser

### Nice-to-haves:
- Environmental inspo/education (imgur api/meme)
- Image slide on homepage(bootsrap)
- Alternate forms of disposal links/info
- Seemless css in all kinds of devices
- Search by image

### won't have:

- Camera capture/recognition
- Schedule of trash/recyle/ other pickup (already an app for that)
