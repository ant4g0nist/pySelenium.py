#!/usr/bin/env python
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def primes_sum(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return sum(primes)


driver = webdriver.Firefox()
driver.get("http://backdoor-problems.cognizance.org.in/misc75/misc75.php")
a=driver.find_element_by_xpath("//p")
b=a.text.split(" ")
answer=primes_sum(int(b[len(b)-4]))
elem = driver.find_element_by_name("answer")
elem.send_keys(answer)
elem.send_keys(Keys.RETURN)
time.sleep(3)
