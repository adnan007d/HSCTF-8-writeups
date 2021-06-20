### BIG-BLIND

# HINT: BLIND

- After visiting the given website you are presented with a login screen.
- I tried basic sleep query to check of it is vulnerable to sql injection `' or sleep(10); -- ` It took around 10 secs to respond and it makes sure that it is vulnerable to sql injection and the title says big-blind means blind sql injection. I used sqlmap to automate the blind injection

```bash
sqlmap https://big-blind.hsc.tf/ --dbms=mysql --forms --crawl=2  --dump --threads 4
```

- After some time it will dump the results

![](flag.png)
