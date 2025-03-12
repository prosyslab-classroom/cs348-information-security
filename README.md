# CS348: 정보보호개론 Introduction to Information Security

## 수업정보 Logistics
- 교수 Instructor: [허기홍 Kihong Heo](https://kihongheo.kaist.ac.kr) (kihong.heo@prosys.kaist.ac.kr)
- 조교 TAs (mailing list: cs348.ta@prosys.kaist.ac.kr)
  - [Tae Eun Kim](https://prosys.kaist.ac.kr/home/taeeunkim) (김태은)
  - [Jaehoon Jang](https://prosys.kaist.ac.kr/home/jaehoonjang) (장재훈)
  - [Minsol Park](https://prosys.kaist.ac.kr/home/minsolpark) (박민솔)
  - [Bongjun Jang](https://prosys.kaist.ac.kr/home/bongjunjang) (장봉준)
- 강의 Time: 월/수 Mon/Wed 09:00 - 10:30
- 장소 Location: N1 117
- 면담 Office hours:
  - 교수 Instructor: Mon 10:30 - 11:30
  - 조교 TAs: Wed 13:00 - 14:00

## 강의 소개 Course Description
이 강의에서는 정보보호 전반에 걸친 기초 내용을 다룬다.
암호, 시스템 보안, 소프트웨어 보안, 웹 보안, 네트워크 보안의 기본 개념을 소개하고
실생활에서 어떠한 보안 위협이 존재하는지 살펴본다.
그리고 이러한 위협으로부터 우리를 보호하는 여러가지 기술에 관해 이야기한다.

본 강의에서는 [쉬운전문용어](https://easyword.kr)를 사용하여 [소박하게 지식을 전달한다](https://prosys.kaist.ac.kr/easy-word/).

This course covers the overall contents of information security. Students will be exposed
to fundamental concepts in information security including cryptography, system security,
software security, web security, and network security. This course introduces how security
attacks occur in modern computing environments. Students will also have opportunities
to understand techniques to discover and disable such security attacks.

## 성적 Grading
- 숙제 Homework: 40%
- 시험 Exam: 40%
- 참여 Participation: 20%
  - 적극적인 참여로 본인이 배운 바를 [스스로 다채롭게 내뿜는](hof.md) 학생들을 위한 보상입니다.
  - This is for students who actively participate and express what they have learned [in a diverse way](hof.md).
  - 매 수업시간에 항상 여러분을 만날 수 있기를 기대합니다. [출석은 정량평가하지 않습니다](https://prosys.kaist.ac.kr/attendance/). 수업에 오는 것은 기본이며, 정량화 할 만큼 가치가 낮지 않기 때문입니다.
  - I always look forward to seeing you in every class. [Attendance is not quantitatively assessed](https://prosys.kaist.ac.kr/attendance/) because it is too valuable to be reduced to a mere number.

## P/NR 관련 공지 Note for P/NR
이 강의는 P/NR 성적을 허용하지 않습니다.
신입생은 반드시 교수에게 이메일을 통해 사전 승인을 받은 후 수강신청하길 바랍니다.

This course DOES NOT allow for P/NR grading.
Freshmen can enroll in this course only if they have prior approval from the instructor.
Send an email to the instructor for approval.

## 교재 Textbook
- 강의자료가 제공됩니다. Lecture slides will be provided
- Ross Anderson, [Security Engineering](https://www.cl.cam.ac.uk/~rja14/book.html) (SE)
- Paul C. van Oorschot, [Computer Security and the Internet](https://people.scs.carleton.ca/~paulv/toolsjewels.html) (CSI)
- J. Katz and Y. Lindell, Introduction to Modern Cryptography (IMC)
- Andreas Zeller et al., [The Fuzzing Book](https://www.fuzzingbook.org) (Fuzzing)
- Xavier Rival and Kwangkeun Yi, [Introduction to Static Analysis: an abstract interpretation perspective](https://library.kaist.ac.kr/search/ctlgSearch/posesn/view.do?bibctrlno=910257&se=b0&ty=B&_csrf=419dcd43-c1b9-4a69-82da-35f631b8777c) (ISA)

## 숙제 Homework
이 강의에서 학생들은 다양한 숙제를 통해 정보보호의 기본 개념을 실제로 익힙니다.
특히 [여기](TOOL.md)에 있는 도구를 사용할 예정입니다.

모든 숙제 제출은 Github와 Gradescope 를 통해서 이루어집니다.
매 숙제마다 제출을 위한 GitHub Classroom 초대 URL이 [게시판](../../discussions)에 공지됩니다.
초대를 수락하면, 여러분의 숙제를 위한 비공개 개인 저장소가 만들어 질 것입니다.
여러분은 제출 기한 이전에 원하는 만큼 해당 저장소에 제출할 수 있고,
이 저장소를 Gradescope에 제출하여 채점결과를 확인할 수 있습니다.

기한을 넘겨서 제출할 시 아래와 같은 규정에 따라 채점합니다:
- 하루 늦을 시 점수의 80%
- 이틀 늦을 시 점수의 50%
- 사흘 이상 늦을 시 0%

모든 프로그래밍 과제는 값 중심 프로그래밍 [[1](http://kwangkeunyi.snu.ac.kr/~kwang/paper/maso/1.html),[2](https://csrc.kaist.ac.kr/blog/2020/08/12/바이너리-분석에-웬-fsharp/)]의 철학과 소프트웨어 개발의 기본 원칙을 따릅니다.
이를 통해 프로그래밍의 즐거움과 고급 개발자의 소양을 함께 느끼게 됩니다.

This course includes written and programming assignments.
Students will use tools described [here](TOOL.md).
All submissions will be managed using Github.
For each assignment, a unique invitation URL for GitHub Classroom will be posted in the [discussion board](../../discussions).
Once you accept the invitation, a private repository for your assignment will be created.
You can push as many commits as you want before the deadline. We will grade the final commit of your `main` branch.

The late homework policy is as follows:
- 80% credit for one day late
- 50% credit for two days late
- NO credit given after two days late

All programming assignments adhere to the philosophy of value-oriented programming [[1](http://kwangkeunyi.snu.ac.kr/~kwang/paper/maso/1.html),[2](https://csrc.kaist.ac.kr/blog/2020/08/12/바이너리-분석에-웬-fsharp/)] and the fundamental principles of software development.
Through this approach, learners experience both the joy of programming and the refined skills of an advanced developer.

## 학문 윤리 Academic Integrity
학문 윤리를 어긴 수강생은 F를 받습니다. 자세한 사항은 [KAIST 전산학부 명예규정](https://cs.kaist.ac.kr/content?menu=309)을 참고하십시오.

세상에 널린 자료 (예: 구글 검색, ChatGPT)를 참고하는 것은 좋지만, 그대로 베끼는 것은 윤리에 어긋납니다.
제출한 과제는 기존 저작물(다른 수강생, 과거 수강생, AI 생성물 등)과 자동으로 비교하여 표절물을 검사합니다.
완전히 본인의 것으로 재창조하지 않고 기존 저작물과 비슷한 경우는 표절로 판단합니다.
이러한 원칙은 AI도구가 등장했다고 해서 달라지지 않습니다.

Students who violate academic integrity will get an F.
See [the KAIST CS honor code](https://cs.kaist.ac.kr/content?menu=309).

It’s fine to refer to readily available resources (e.g., Google searches, ChatGPT), but copying them directly is unethical. Submitted assignments will be automatically compared to existing works (other students’ work, past students’ work, AI-generated content, etc.) to check for plagiarism. If the work closely resembles existing material without being fully recreated as your own, it will be considered plagiarism. This principle remains unchanged even in the AI era.

## 강의 계획 Schedule
|#|Topics|Reading|Homework|
|-|------|-------|--------|
|0|[Functional Programming in OCaml](slides/lecture0.pdf)||HW0: Hello-world, OCaml programming|
|1|[Introduction](slides/lecture1.pdf)||
|2|[Concepts in Security](slides/lecture2.pdf)||
|3|[Classical Cryptography](slides/lecture3.pdf)|IMC Ch1|HW1: Classical Cryptography|
|4|[Symmetic-key Encryption](slides/lecture4.pdf)|IMC Ch2, Ch3, [AES Visualization](https://formaestudio.com/rijndaelinspector/archivos/Rijndael_Animation_v4_eng-html5.html)|HW2: Mini-AES|
|5|[Message Integrity](slides/lecture5.pdf)|IMC Ch4, [<img src="icons/youtube.png" width="16" /> Birthday Paradox](https://youtu.be/KtT_cgMzHx8)|HW3: Mini-SHA|
|6|[Availability](slides/lecture6.pdf)|||
|7|[Public-key Cryptography](slides/lecture7.pdf)|IMC Ch11, Ch12, Ch13, [<img src="icons/youtube.png" width="16" /> Diffie-Hellman](https://www.youtube.com/watch?v=YEBfamv-_do)|HW4: Mini-RSA|
|8|[Access Control](slides/lecture8.pdf)|[Zelkova](https://www.amazon.science/blog/a-billion-smt-queries-a-day)|HW5: Access Control System|
|9|[Web Security](slides/lecture9.pdf)|CSI Ch9||
|10|[Software Vulnerabilities](slides/lecture10.pdf)||HW6: Exploitation|
|11|[Safe Programming Systems](slides/lecture11.pdf)|<img src="icons/youtube.png" width="16" /> Undecidability [<img src="icons/kor.png" width="16" />](https://youtu.be/oippSXvxUlw) [<img src="icons/eng.png" width="16" />](https://www.youtube.com/watch?v=HeQX2HjkcNo&t=2)||
|12|[Dynamic Analysis and Fuzzing](slides/lecture12.pdf)||HW7: Fuzzer|
|13|[Static Analysis](slides/lecture13.pdf)|[CACM'19](https://cacm.acm.org/magazines/2019/8/238344-scaling-static-analyses-at-facebook/fulltext?mobile=false), [Zoncolan](https://engineering.fb.com/2019/08/15/security/zoncolan/)|HW8: Static Analyzer|
|-|Final Exam||

## 명예의 전당 Hall of Fame
지난 학기 수강생들이 [남긴](https://prosys.kaist.ac.kr/what-is-left/) 멋진 작품을 [여기서](hof.md) 감상해 보세요 (에세이, 그림 등).

See the outstanding achievement of our friends [here](hof.md).

## 심화 과목 Advanced Course
- [CS492: Program Reasoning](https://github.com/prosyslab-classroom/cs492-program-reasoning)
- [CS524: Program Analysis](https://github.com/prosyslab-classroom/cs524-program-analysis)

## 감사 Acknowledgment
이 강의 자료의 일부는 KAIST 강민석, 차상길 교수님의 강의록을 참고하여 작성하였습니다.

A large part of the slides is based on the lecture notes of Prof. Min Suk Kang and Prof. Sang Kil Cha at KAIST.

## 참고 자료 References
#### 기본 Preliminaries
- [PL Wiki](https://github.com/prosyslab/pl-wiki/wiki)
- [Automated Reasoning @ Amazon](https://www.amazon.science/blog/?q=&f0=0000017d-6ba3-ddaa-a97d-efa3e2ed0000&s=0&expandedFilters=Research%2520area%2CTag%2CConference%2CAuthor%2CDate%2C)
- [BugSynth](https://prosys.kaist.ac.kr/bugsynth/)
- [Recursion World](http://recursion.kaist.ac.kr)

#### 암호 Cryptography
- [Formal Verification Makes RSA Faster and Faster to Deploy](https://www.amazon.science/blog/formal-verification-makes-rsa-faster-and-faster-to-deploy)
- [현대암호학의 태동 1: 고전암호학](https://horizon.kias.re.kr/30970/)
  
#### 안전한 프로그래밍 언어 Secure Programming Languages
- [Memory Safety](https://www.chromium.org/Home/chromium-security/memory-safety/), Google
- [OCaml: Memory Safety and Beyond](https://tarides.com/blog/2023-12-14-ocaml-memory-safety-and-beyond/), Tardes 2023
- [Programming Language and Cybersecurity](https://tarides.com/blog/2023-08-17-your-programming-language-and-its-impact-on-the-cybersecurity-of-your-application/), Tardes 2023
- [Principles and Practices for SW Memory Safety](https://cacm.acm.org/opinion/it-is-time-to-standardize-principles-and-practices-for-software-memory-safety/), CACM 2025
- [Future Software Should Be Memory Safe](https://bidenwhitehouse.archives.gov/oncd/briefing-room/2024/02/26/press-release-technical-report/), White House

#### 프로그램 분석과 검증 Program Analysis & Verification
- [Infer](https://fbinfer.com)
- [CodeQL](https://codeql.github.com)
- [Lessons from Building Static Analysis Tools at Google](https://dl.acm.org/doi/10.1145/3188720), CACM 2018
- [Scaling Static Analysis at Facebook](https://cacm.acm.org/magazines/2019/8/238344-scaling-static-analyses-at-facebook/fulltext), CACM 2019
- [Detect Bugs Early with the Static Analyzer](https://developer.apple.com/videos/play/wwdc2021/10202/), Apple WWDC 2021
- [Formal Software Verification Measures Up](https://dl.acm.org/doi/10.1145/3464933), CACM 2021
- [Automated Reasoning @ Amazon](https://www.amazon.science/blog/?q=&f0=0000017d-6ba3-ddaa-a97d-efa3e2ed0000&s=0&expandedFilters=Research%2520area%2CTag%2CConference%2CAuthor%2CDate%2C)
