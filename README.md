# CS348: Introduction to Information Security (정보보호개론)

## Logistics
- Instructor: [Kihong Heo](https://kihongheo.kaist.ac.kr) (허기홍, kihong.heo@prosys.kaist.ac.kr)
- TAs (mailing list: cs348.ta@prosys.kaist.ac.kr)
  - [Yeonhee Ryou](https://yeonhee-ryou.github.io) (류연희)
  - [Jongchan Park](https://kaist-jongchanpark.github.io) (박종찬)
  - [Sujin Jang](https://sujin0529.github.io) (장수진)
- Time: Mon/Wed 09:00 - 10:30
- Location: N1 117
- Office hour:
  - Instructor: Mon 10:30 - 11:30
  - TAs: Wed 13:30 - 14:20

## Course Description
This course covers the overall contents of information security. Students will be exposed
to fundamental concepts in information security including cryptography, system security,
software security, web security and network security. This course introduces how security
attacks occur in the modern computing environments. Students will also have opportunities
to understand techniques to discover and disable such security attacks.

## Grading
- Homework 50%
- Exam 40%
- Participation 10%

Notice that *participation* does not mean *attendance* but includes various [activities](hof.md) during the semester.
There is no [*attendance score*](https://prosys.kaist.ac.kr/attendance/) because attendence is expected by default.


## Textbook
- Lecture slides will be provided
- Ross Anderson, [Security Engineering](https://www.cl.cam.ac.uk/~rja14/book.html)
- Paul C. van Oorschot, [Computer Security and the Internet](https://people.scs.carleton.ca/~paulv/toolsjewels.html)
- Andreas Zeller et al., [The Fuzzing Book](https://www.fuzzingbook.org)
- Xavier Rival and Kwangkeun Yi, [Introduction to static analysis : an abstract interpretation perspective](https://library.kaist.ac.kr/search/ctlgSearch/posesn/view.do?bibctrlno=910257&se=b0&ty=B&_csrf=419dcd43-c1b9-4a69-82da-35f631b8777c)

## Homework
This course includes written and programming assignments.
Students will use a few tools which are described [here](TOOL.md).
All submissions will be managed using Github.
For each assignment, a unique invitation URL for Github Classroom will be posted in the [issue board](../../issues).
Once you accept the invitation, a private repository for your assignment will be created.
You can push as many commits as you want before the deadline. We will grade the final commit of your `main` branch.

The late homework policy is as follows:
- 80% credit for one day late
- 50% credit for two days late
- NO credit given after two days late

## Academic Integrity Violation
Students who violate academic integrity will get F. See [the KAIST CS honor code](https://forms.gle/mxApoGi1vMkcCJ7n8).

## Schedule
|#|Topics|Reading|Homework|
|-|------|-------|--------|
|0|[Functional Programming in OCaml](slides/lecture0.pdf)||HW0: Hello-world, OCaml programming|
|1|[Introduction](slides/lecture1.pdf)||
|2|[Concepts in Security](slides/lecture2.pdf)||
|3|[Classical Cryptography](slides/lecture3.pdf)||HW1: Classical Cryptography|
|4|[Symmetic-key Encryption](slides/lecture4.pdf)||HW2: Mini-AES|
|5|Message Integrity|||
|6|Availability|||
|7|Public-key Encryption||HW3: Mini-RSA|
|8|Secure Channel||
|9|[Access Control](slides/lecture14.pdf)|[Zelkova](https://www.amazon.science/blog/a-billion-smt-queries-a-day)|HW4: Access Control Verifier|
|10|[Web Security](slides/lecture15.pdf)|||
|11|[Software Vulnerabilities](slides/lecture16.pdf)||HW5: Exploitation|
|12|[Safe Programming Systems](slides/lecture17.pdf)|||
|13|[Fuzzing](slides/lecture18.pdf)||HW6: Fuzzer|
|14|[Static Analysis](slides/lecture19.pdf)|[CACM'19](https://cacm.acm.org/magazines/2019/8/238344-scaling-static-analyses-at-facebook/fulltext?mobile=false), [Zoncolan](https://engineering.fb.com/2019/08/15/security/zoncolan/)|HW7: Static Analyzer|
|-|Final Exam||

## Hall of Fame
See the outstanding achievement of our friends [here](hof.md).

## Advanced Course
- [CS492: Program Reasoning](https://github.com/prosyslab-classroom/cs492-program-reasoning)
- [CS524: Program Analysis](https://github.com/prosyslab-classroom/cs524-program-analysis)

Acknowlegement

A large part of the slides is based on the lecture notes of Prof. Min Suk Kang at KAIST.

## References
- [PL Wiki](https://github.com/prosyslab/pl-wiki/wiki)
- [Automated Reasoning @ Amazon](https://www.amazon.science/blog/?q=&f0=0000017d-6ba3-ddaa-a97d-efa3e2ed0000&s=0&expandedFilters=Research%2520area%2CTag%2CConference%2CAuthor%2CDate%2C)
