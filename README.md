# CS348: Introduction to Information Security (정보보호개론)

## Logistics
- Instructor: [Kihong Heo](https://kihongheo.kaist.ac.kr) (허기홍, kihong.heo@kaist.ac.kr)
- TAs (mailing list: cs348.ta@prosys.kr)
  - 
- Time: Mon/Wed 09:00 - 10:30
- Location: N1 117
- Office hour:
  - Instructor: Mon 10:30 - 11:30
  - TAs: TBD

## Course Description
This course covers the overall contents of information security. Students will be exposed
to fundamental concepts in information security including cryptography, system security,
software security, web security and network security. This course introduces how security
attacks occur in the modern computing environments. Students will also have opportunities
to understand techniques to discover and disable such security attacks.

## Grading
- Exam 50%
- Homework 40%
- Participation 10%

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
Students who violate academic integrity will get F. See [the KAIST CS honor code](https://docs.google.com/forms/d/e/1FAIpQLSdSn63tEvq6R0G6n3Cz7jKX16RWvDy2giBKm8EVJtQHUBJoDA/viewform).

## Schedule
|#|Topics|Reading|Homework|
|-|------|-------|--------|
|0|[Functional Programming in OCaml](slides/lecture0.pdf)|HW0: Hello-world, OCaml programming|
|1|Introduction||
|2|Concepts in Security||
|3|Symmetic-key Encryption||HW1: Cryptogram Cracker|
|4|Public-key Encryption||
|5|Authentication||
|6|Secure Channel||
|-|Midterm Exam||
|7|[Access Control](slides/lecture14.pdf)|[Zelkova](https://www.amazon.science/blog/a-billion-smt-queries-a-day)|HWx: Access Control Verifier|
|8|[Web Security](slides/lecture15.pdf)|||
|9|[Software Vulnerabilities](slides/lecture16.pdf)|||
|10|[Safe Programming Systems](slides/lecture17.pdf)|||
|11|[Fuzzing](slides/lecture18.pdf)||HWx: Fuzzer|
|12|[Static Analysis](slides/lecture19.pdf)||HWx: Static Analyzer|
|-|Final Exam||

## Hall of Fame
See the outstanding achievement of our friends [here](hof.md).

## Advanced Course
- [CS492: Program Reasoning](https://github.com/prosyslab-classroom/cs492-program-reasoning)
- [CS524: Program Analysis](https://github.com/prosyslab-classroom/cs524-program-analysis)

## References
- [PL Wiki](https://github.com/prosyslab/pl-wiki/wiki)
- [Automated Reasoning @ Amazon](https://www.amazon.science/blog/?q=&f0=0000017d-6ba3-ddaa-a97d-efa3e2ed0000&s=0&expandedFilters=Research%2520area%2CTag%2CConference%2CAuthor%2CDate%2C)
