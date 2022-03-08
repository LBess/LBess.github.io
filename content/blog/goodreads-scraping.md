---
title: All I Wanted was a Currently Reading Section
description: A discussion on how I added the section on my website to show what I'm currently reading.
date: "2022-03-07T00:00:00+00:00"
publishDate: "2022-03-07T00:00:00+00:00"
---

## Introduction

This is a story about how I added a currently reading section to my website.

Last summer one of my friends was showing me his website. He liked reading books as well, and had a nice little widget on the homepage that synced up to his Goodreads
account and displayed the books he was currently reading. I thought, "Huh, that's neat. I'll need to add that to my website at some point."

Fast forward to February 2022, and I'm arriving back to the States from a backpacking trip in Argentina. I've seen too much nature the past month and want to
do some coding. I recall how I wanted to showcase the books I'm currently reading by hooking up my website to my Goodreads account. Great, let's do it!

![Stack of Books](/blog/images/stack-of-books.jpg)

## Development

The first thing I did was to look into the [Goodreads API](https://www.goodreads.com/api). This didn't get very far, because at the very top of the webpage Goodreads says:
"As of December 8th 2020, Goodreads no longer issues new developer keys for our public developer API and plans to retire the current version of these tools".

Okay great, no problem (I think). What if I just scraped the books I'm reading from Goodreads by downloading the page and parsing the HTML?
At first I tried doing this with Javascript, for obvious reasons. If the Javascript runs when my website is loaded, scrapes Goodreads, then adds the
corresponding books to my website's HTML code, then problem solved! 

I faced two problems with this. The first was my lack of experience with web development and Javascript in general. 
The second, and related, issue was that of [CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS/Errors). Essentially, I threw together a Javascript to do the scraping, 
but when I tried to run this on my local server I just got CORS request failures. Okay no problem, I'll just look it up on Stackexchange. The problem I then faced was that
I was building my project via [Hugo](https://gohugo.io/) (a static site generator) and running a local Hugo server. 
I unfortunately could not find a way to remedy the CORS issue by modifying the Hugo server, 
and didn't want to bother pushing the site to Github pages each time to see if my Javascript code was working.

After getting fed up with CORS, I recalled that there were these wonderful things called [Github Actions](https://github.com/features/actions), and that I could also do 
scraping with Python's Beautiful Soup library. So, I wrote up a Python script to do the scraping and changing the website's HTML. 
Then I started researching how to make my own Github actions. My idea here was this - the Python script will run on a schedule, say once a week, 
and commit its changes (i.e. the books it gets from my Goodreads webpage). Then, another Github action will run Hugo to build my website again
and deploy it to Github Pages (the website hosting platform).

Github actions have come a long way from when I first tried using them (for a few minutes) a number of years ago. Now they have good documentation and an awesome
GUI to show you their progression. That being said, my understanding is that to test them, you have to push them to the repository (or a test repository).
If I was covering all my bases I ought to have made another branch and done my Github action testing there, but 1) this is my repo and I do what I want!
2) I didn't really think of it at the time, I thought it'd be quicker than it was.

Thankfully there were others before me who thought to use Github actions to automate their Hugo workflow (albeit without this archaic Python scraper by yours truly).
This meant I could use an action someone else made to run Hugo and build the site, then create another action for my scraper. The most time consuming bug I ran into
was that the step that built the Hugo project was storing the files in the root directory, instead of `public/`. Github Pages was looking for files in the `public/`
directory to publish - which was empty - so the site was looking a bit barren. This problem was hard to debug because 1) the built files aren't commited to the main
branch, so there was no trace of them 2) other examples of using Github actions to build Hugo projects didn't seem to have this issue, or their projects were just set
up a bit differently than mine.

![Stack of Books](/blog/images/github-actions.png)

## Conclusion

Was this overengineered? Yes. Did it take more work than it needed to? Undoubtedly. Did I learn and ton and feel awesome when I finally got it to work? Absolutely.

If I were to do this again I'd probably just stick with Javascript, but honestly, I'm glad I took this roundabout path.

Anyhow, this is a long-winded post to document my strange adventure of adding a currently reading section to my website, such that now that it's deployed, I won't
have to do anything for it to update (Unless of course we lose Github actions or Goodreads)!
