# Linux Bash Challenge

Below are a couple of additional challenges on bash scripting

# Question 1

Regex is great because of the ability to extract information from unstructured sources
(instead of relying on delimiters). To demonstrate, write a script that extracts all
thumbnail images from a particular subreddit.

<ol type='a'>

<li>
Come up with a bash one-liner that extracts all the image URLs from
https://old.reddit.com/r/aww.json where the domain name contains
thumbs.redditmedia.com and ends with png, jpg, or gif.  For example, the
following is a partial result of my output:

```
https://b.thumbs.redditmedia.com/r1W69Teu5AoQHhWZxZHVoaNrv988hoWykke3hKpPuUk.jpg
https://b.thumbs.redditmedia.com/WU0F9g5eTEzE8oQUS4sKEdbmMPLwvkf-ECa6Job6C7M.jpg
https://b.thumbs.redditmedia.com/AEpeomHhYUq9XNX-obDtTNQ6aNSy1GdVWirFjRFrLOA.jpg
https://b.thumbs.redditmedia.com/TVdfyzoeyTPPf5I2HzmT--StxZXDCwrqIXPNTBORnQg.jpg
https://b.thumbs.redditmedia.com/M_dVA0A2bB2uNVT2cHEafud8ZeUZs4E3zr6aWIgSrXc.jpg
https://b.thumbs.redditmedia.com/Db8awsyCygCns_SZaAC-TkJjUSOZ5y-SHq3ah7ykMXo.jpg
https://a.thumbs.redditmedia.com/-ZCBL9kb3CkcvEEX4MvPaFvz6HrQJfXs-_BWoWmT8t4.jpg
https://b.thumbs.redditmedia.com/bDqMbtITM9oNO4bGjb1YQ-01TsVRkfWa-jQ9MUkPzis.jpg
https://a.thumbs.redditmedia.com/fP0UFhpuS2fSH5REgnEp6B5DItL87Odu1LJhYVO59b8.jpg
https://a.thumbs.redditmedia.com/3N9_bGg4Z6nYTVDe7U_6dfUitNzodQ_nlDL76RhmqZ8.jpg
https://b.thumbs.redditmedia.com/gu1BrFdWRbLP9uWVbIC2RTvcTR8D8BG2_xsBJywuieE.jpg
https://a.thumbs.redditmedia.com/9d_Q0rLAfJaoLL26G_aZ-rD6g477d2BG5O9Y_T9jfP0.jpg
https://b.thumbs.redditmedia.com/gD_k_uIWUIfWZazsT7t6_tBrzrdrxm0q2g4PLsFgwzM.jpg
https://b.thumbs.redditmedia.com/2tMkGTbdPlaZ4tmIPMtaX8jDCiulkAVZRD6Om6ptRdE.jpg
https://b.thumbs.redditmedia.com/T_PG0G7oMDdU0QTPBl5KYTYj3SnM-zQ6jQNKc6ocN9E.jpg
https://b.thumbs.redditmedia.com/N6-K-_V978-M3HvfE0yh8NeJ1w-QHfbEBcdntXNN88E.jpg
https://b.thumbs.redditmedia.com/g2AHWlZbeLo3sVLn2DNcR1tlJCdZY8_6f2lhXlP_B-o.jpg
```

Put this one-liner into the file **`q1a.txt`**
</li>

<li>
Create a script file called <pre><em>extract_thumbs.sh</em></pre> that takes a subreddit
as an argument.  Running ./extract_thumbs.sh aww will save all thumbnails
(i.e. the JSON key being "thumbnail") from the https://www.reddit.com/r/aww.json
into the subdirectory thumbs_aww/

![extract_thumbs.sh](images/image4.gif)
</li>

<li>
Modify your script to handle multiple command line arguments, as below:

Here’s how you can process multiple arguments:
https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script#loop-construct 

![extract_thumbs multiple arguments](images/image3.png)
</li>

</ol>

# Question 2

When visiting a website, sometimes you will be asked for a user-id and
password combo.  The website that we will be using in this exercise is
https://learn.operatoroverload.com/~jmadar/protected/index.html.
If you visit it with a browser, you will be prompted for proper credentials
via a dialog box, as follows:

![basic auth with browser](images/image1.gif)

The above interaction can be done via curl:

![basic auth with curl](images/image8.png)

Pay special attention to how username and passwords are included in the url.
The username for our targeted website will always be www-user, but the
password is randomly chosen from the first 100 lines in this file:
https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10k-most-common.txt 

Write a script **`brute_force.sh`** that extracts the message enclosed inside the
&lt;h1%gt; tag from the password protected page and outputs it to stdout.  The
script will accomplish this by trying the 100 potential passwords, one at a time.  

![brute force password hacking](images/image7.gif)

## HINTS

The secret message is different from the screen caps shown in the lab write-up.
After all, it's a "secret message".  So the most effective way to detect if you
got the secret message is to test for the ABSENCE of the string '401 Unauthorized"
in the output.

# Hand-in

If you completed the entire assignment, you will have the following files
in your assignment directory:

- q1a.txt
- extract_thumbs.sh
- brute_force.sh

Make sure you run `pytest` to check your score.

Once you are satisified with your score, run the following commands to submit your assignment:

1. `git add -A`
2. `git commit -a -m 'submit'`
3. `git push`
