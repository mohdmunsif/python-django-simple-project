# Project 4

What I had agreed in to do in the submitted Google Doc.
ToysForYou

The app is meant for parents to find suitable age-appropriate toys for their kids, with other users recommending toys and reviews.

1. User Registration, 2. User Login (all validation included). 3. Page to submit toy recommendation (with age range), and possibly link to buy such toy

2. All the previous ones, + 4. feature to upload user photos

3. all the previous ones, + 5. usual user/login feature, security stuff (all link is guarded), authentication, password reset, 6. I do not know how to do this yet, but upon submission of URL from Walmart, or Amazon perhaps, some snippet of the URL will be stored and displayed (like how Facebook snippet works for links)

4. Need to research what Python framework would help me the most - right now my mindset is still on Flask but as i go along with Django, i might choose it if i think it would make the most sense based on its feature vs flask. New skills: development a proper webapp using Django or Flask, with user uploading stuff


COMMENTS:
1. Users can register, with validation
2. All URLs would require authentication
3. Users can submit Toys recommendation, adding URL and 1 image
4. Users can use the search bar to search either Toyname or Toy Description
5. On the browse page, users can filter results based on Age interested.
6. Main page contains pagination that will split the result based
7. While it is not apparent, clicking on the toyname would load the individual toy result - which i wanted to use as a page where users can enter reviews, ratings and comments.
8. I was not able to do a password reset yet.
9. Two issues (bug really):
A. pagination will use the current URL path, which is
changed after user do searches, i need to modify the View to accommodate this but need to think of a way to do so.
B. The image, when loading a toy page, did not load as it is referring to URL relative to
the toy page so probably the same issue as A.

10. I feel my views contains some redundancy, which i believe i can reduce the number of views by doing something clever. Nothing comes to mind yet.

I managed to re-use the code in project3, with a couple of addition, searching, pagination, uploading images. Form validation and manipulation works.
