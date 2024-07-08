# Linux Bash Challenge

Below are a couple of additional challenges on bash scripting

# Question 1

Regex is great because of the ability to extract information from unstructured sources
(instead of relying on delimiters). To demonstrate, write a script that extracts all
thumbnail images from a WordPress based website.

WordPress is a popular "Content Management System" that helps users setup websites
and blogs.  Many of the major websites including NASA (https://www.nasa.gov) and
time magazine (https://time.com/) are created using WordPress.

It turns out that, for some WordPress websites, you can append the string
`wp-json/wp/v2/posts/?per_page=10&context=embed` to the URL to get JSON formatted
data for the website.  For example:

https://www.nasa.gov/wp-json/wp/v2/posts/?per_page=10&context=embed

and

https://time.com/wp-json/wp/v2/posts/?per_page=10&context=embed

Will give you the JSON data for the first 10 posts on the page.

<ol type='a'>

<li>
Come up with a bash one-liner that extracts all the image URLs from
the popular tech news website Techcrunch.  The full URL is here:

https://techcrunch.com/wp-json/wp/v2/posts?per_page=10&context=embed

We want full URL that starts with https ends with png, jpg, or gif.
For example, the following is a partial result of my output:

```
$ curl -s 'https://techcrunch.com/wp-json/wp/v2/posts?per_page=10&context=embed' | ${this_is_what_you_need_to_figure_out}
https://techcrunch.com/wp-content/uploads/2018/04/tc-logo-2018-square-reverse2x.png
https://techcrunch.com/wp-content/uploads/2020/09/7-1.jpg
https://techcrunch.com/wp-content/uploads/2022/05/GettyImages-95769788.jpg
https://techcrunch.com/wp-content/uploads/2024/07/GettyImages-1917798465.jpg
https://techcrunch.com/wp-content/uploads/2024/07/GettyImages-520120864.jpg
https://techcrunch.com/wp-content/uploads/2024/07/Scribble-Journey.png
https://techcrunch.com/wp-content/uploads/2024/07/amazon-echo-spot.jpg
https://techcrunch.com/wp-content/uploads/2024/07/pestle-instagram.jpg
```

Put this one-liner into the file **`q1a.txt`**
</li>

<li>
Create a script file called <strong><code>extract_images.sh</code></strong> that
takes a valid WordPress as an argument.  Running ./extract_images.sh techcrunch.com will
save all images from the https://techcrunch.com into the subdirectory
`downloads.techcrunch.com`

See below for the terminal interaction:

```
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ls -l
total 20
-rw-rw-r-- 1 ubuntu ubuntu 5439 Jul  8 18:57 README.md
-rwxr-xr-x 1 ubuntu ubuntu  229 Jul  8 18:54 extract_images.sh
drwxrwxr-x 2 ubuntu ubuntu 4096 Jul  8 18:07 images
drwxrwxr-x 2 ubuntu ubuntu 4096 Jul  8 18:07 tests
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ./extract_images.sh techcrunch.com
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ls -l
total 24
-rw-rw-r-- 1 ubuntu ubuntu 5439 Jul  8 18:57 README.md
drwxrwxr-x 2 ubuntu ubuntu 4096 Jul  8 18:58 downloads.techcrunch.com
-rwxr-xr-x 1 ubuntu ubuntu  229 Jul  8 18:54 extract_images.sh
drwxrwxr-x 2 ubuntu ubuntu 4096 Jul  8 18:07 images
drwxrwxr-x 2 ubuntu ubuntu 4096 Jul  8 18:07 tests
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ls -l downloads.techcrunch.com/
total 12056
-rw-rw-r-- 1 ubuntu ubuntu 8853337 Sep 14  2022 7-1.jpg
-rw-rw-r-- 1 ubuntu ubuntu  969876 Sep 14  2022 GettyImages-95769788.jpg
-rw-rw-r-- 1 ubuntu ubuntu  452792 Jul  8 14:28 Scribble-Journey.png
-rw-rw-r-- 1 ubuntu ubuntu  223934 Jul  8 16:30 amazon-echo-spot.jpg
-rw-rw-r-- 1 ubuntu ubuntu  880875 Jul  8 14:25 pestle-instagram.jpg
-rw-rw-r-- 1 ubuntu ubuntu  187369 Sep 14  2022 tc-logo-2018-square-reverse2x.png
-rw-rw-r-- 1 ubuntu ubuntu  762770 Jul  8 18:16 vladimir-putin-russia-kremlin.jpg
```
</li>

<li>
Create a script called <strong><code>extract_images_2.sh</code></strong>.  This script will take multiple WordPress
websites as command line arguments and extract each site's images into their own
downloads subdirectories.  As follows:

```
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ls
README.md  extract_images.sh  extract_images_2.sh  images  tests
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ./extract_images_2.sh techcrunch.com www.nasa.gov
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ls
README.md  downloads.techcrunch.com  downloads.www.nasa.gov  extract_images.sh  extract_images_2.sh  images  tests
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ ls downloads.*
downloads.techcrunch.com:
7-1.jpg                   Scribble-Journey.png  pestle-instagram.jpg               vladimir-putin-russia-kremlin.jpg
GettyImages-95769788.jpg  amazon-echo-spot.jpg  tc-logo-2018-square-reverse2x.png

downloads.www.nasa.gov:
enosechallenge.png  grc-2006-c-01777orig.jpg  sandyastrov2-16x9-0.jpg  webb-stsci-01j0by7f04dahq55zjq4wcdbrz-2k-.png
ubuntu@ip-172-31-28-86:~/linux-bash-challenge$ 
```

## HINTS

1. Here’s how you can process multiple arguments:
   https://www.baeldung.com/linux/use-command-line-arguments-in-bash-script#loop-construct

2. The best strategy to use is for extract_images_2.sh to call extract_images.sh in a loop.
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
- extract_images.sh
- extract_images_2.sh
- brute_force.sh

Make sure you run `pytest` to check your score.

Once you are satisified with your score, run the following commands to submit your assignment:

1. `git add -A`
2. `git commit -a -m 'submit'`
3. `git push`
