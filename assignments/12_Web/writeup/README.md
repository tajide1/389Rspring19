# Crypto II Writeup

Name: Oluwatobi Ajide
Section: 0201

I pledge on my honor that I have not given or received any unauthorized
assistance on this assignment or examination.

Digital acknowledgement: Oluwatobi Ajide

## Assignment Writeup

### Part 1 (40 Pts)
Using the sql injection of   ' || '1' = '1  broght up the flag. Which was CMSC389R-{y0u_ar3_th3_SQ1_ninj@}. It is always the basic sql injection i always 
used to kind of a response from sql database.
### Part 2 (60 Pts)
1. This was a basic which required a basic script tag which was <script> alert('hello') </script>
2. Script can't be used here so I decided to use the img tag oneerror. Which would include the "javascript:alert("hello")"
3. In the index.html I found out that the num in html += "<img src='/static/level3/cloud" + num + ".jpg' />" could my accces point to gettin gthe 
	 alert into the url so I tried ' oneerror="alert('hello')"
4.
