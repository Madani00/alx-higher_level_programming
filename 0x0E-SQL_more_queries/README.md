## How to import a SQL dump
```yaml
$ echo
 "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

![Alt text](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.educba.com%2Fjoins-in-mysql%2F&psig=AOvVaw0ET-6QYMRSBmk5uFubL2pb&ust=1710619457234000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJjo9p6I94QDFQAAAAAdAAAAABAE)
