# Fancy Index

A responsive Apache index page.

I was tired of seeing the ugly apache-generated index page, so I decided to do something about it. Inspired by [Seti UI](https://github.com/jesseweed/seti-ui) and [atom file-icons](https://github.com/file-icons/atom), this project adds an `.htaccess` file which tells apache to use a table, among other things, instead of `<pre>`.

`This version allows for icons to be replaced with thumbnails on image and pdf files. It also includes a thumbnailer to use when dealing with larger images.`

### Before Fancy Index:
![before fancy index](before.png)

### After Fancy Index
![after fancy index](after.png)


## Setup

1. Clone `fancy-index` repo into /var/www/html or sub directory as desired (instructions will assume this directory).

2. Move `images`, `thumbnailer.py`, and `.htaccess` up one level (/var/www/html).

3. Edit /etc/httpd/conf.d/welcome.conf so that every line is commented out.

4. Edit /etc/httpd/conf.d/userdir.conf so that the final lines read:

`<Directory "/var/www/html">
    AllowOverride All
    Options MultiViews Indexes FollowSymLinks
    Require all granted
</Directory>`

5. Restart httpd

6. Run `thumbnailer.py` so that thumbnails in `images` will appear. 
-Thumbnailer uses imagemagick. Ensure this is installed on your system.
-Thumbnailer requires an argument specifying the root directory for images to convert. 
ex:`python thumbnailer.py /var/www/html/images`

7a. Create cron job to run `thumbnailer.py`.
      ex.  `* 16 * * * /usr/bin/python /var/www/html/thumbnailer.py <path>`
7b. Manually run `thumbnailer.py` after each change to `images` directory.

8. Drink all the beer!

## Mobile Comparison

Now you don't have to zoom in or be a sniper with your finger!

| Default  | Fancy  |
|:--------:|:------:|
|![before fancy index (mobile)](before_mobile.png)  |  ![after fancy index (mobile)](after_mobile.png)|

## Customizing hidden files and directories

If you want to hide some files or directories, for example the `fancy-index` directory, there is a `IndexIgnore` directive in `.htaccess` file.

1. Edit `.htaccess` file in root directory.
2. Look for the "IGNORE THESE FILES" section.
3. Update the `IndexIgnore` directive with the path of files and directories to hide, separated by spaces.
	* For example: `IndexIgnore .ftpquota .DS_Store .git /fancy-index`
4. Save the changes.
5. Reload the index page.
