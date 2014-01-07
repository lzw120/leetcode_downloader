#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
import os
import mechanize

from bs4 import BeautifulSoup



LEET_CODE_DOMAIN = 'oj.leetcode.com'

LOGIN_URL = 'http://' + LEET_CODE_DOMAIN + '/accounts/login/'

class NotLoginException(Exception):
    pass

class LeetCodeDownloader:

    def __init__(self, name, password):
        br = mechanize.Browser()
        br.open(LOGIN_URL)

        br.select_form(nr = 0)

        br['login'] = name
        br['password'] = password

        r = br.submit()
        if r.geturl() == LOGIN_URL:
            raise NotLoginException

        self.br = br

    def load_accepted_problems(self):
        r = self.br.open('/problems/')
        soup = BeautifulSoup(r.read())
        problems = soup.select('#problemList tbody tr')
        for prob in problems:
            cols = prob.findAll('td')

            status = cols[0].find('span')['class']
            
            if not 'ac' in status:
                continue

            link = cols[1].find('a')['href']
            title = cols[1].find('a').string

            yield (link, title)


    def load_accepted_submission_ids(self, prob_link):
        r = self.br.open(prob_link + '/submissions/')
        soup = BeautifulSoup(r.read())

        submissions = soup.select('a.status-accepted')

        for submission in submissions:
            yield submission['href'].strip('/').split('/')[-1]

    def read_code_by_submission_id(self, subid):
        r = self.br.open('/submissions/detail/' + subid + '/')
        soup = BeautifulSoup(r.read())

        language = soup.select('#result_language')[0].string
        code = soup.select('textarea')[0].string

        return (code, language)



if __name__ == '__main__':

    if len(sys.argv) < 3:
        print """Leetcode Downloader

Usage:
%s username password
        """ % sys.argv[0]


    leetcodedownloader = LeetCodeDownloader(sys.argv[1], sys.argv[2])

    for link, title in leetcodedownloader.load_accepted_problems():

        print 'Downloading accepted problem %s'  % title

        dirname = link.strip('/').split('/')[-1] 

        if not os.path.exists(dirname):
            os.mkdir(dirname)
        elif not os.path.isdir(dirname):
            print "Dirname conflict"
            sys.exit(1)


        for subid in leetcodedownloader.load_accepted_submission_ids(link):
            code, language = leetcodedownloader.read_code_by_submission_id(subid)

            filename = dirname + '/Solution.' + subid + '.' + language
            print 'Writing to %s' % filename

            f = open(filename, 'w')
            f.write(code.encode('utf8'))
            f.close()



