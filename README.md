Leetcode Downloader
===================

Downloader for your accpeted [leetcode oj](http://oj.leetcode.com/) submissions

Dependency
----------

 * [mechanize](http://wwwsearch.sourceforge.net/mechanize/)
 * [beautifulsoup4](http://www.crummy.com/software/BeautifulSoup/)

just run `pip install -r requirements.txt` to install them

Usage
-----

Downloader will fetch your `ACCEPTED` submissions into respective dir based on problem name

    ./leetcode_downloader.py YOURNAME YOUR_PASSWOD
    
    Downloading accepted problem Linked List Cycle
    Writing to linked-list-cycle/Solution.993783.java
    
    $ tree
    .
    ├── add-binary
    │   └── Solution.665166.java
    ├── add-two-numbers
    │   └── Solution.666385.java
    ├── balanced-binary-tree
    │   └── Solution.660938.java
    ├── best-time-to-buy-and-sell-stock
