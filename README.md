# Index Pluggable Study
By: Madeline Wessels, Jasper Hugunin, Matthew Staehely

A case study being performed on the Index Checker pluggable tool, from a programmer's perspective.
This case study is looking to examine the effectiveness and efficiency of the index checker tool, with
respect to defect prevention and time saved or spent using the annotation system provided by the tool.

The case study will be performed on two separate codebases. The first is the Joda-Time codebase, located
at https:www.github.com/JodaOrg/joda-time. The second codebase will be the Google Collections framework,
referred to as Guava. These codebases will be annotated using the Index Checker to analyze the ease of 
use of the index checker on already existing, well-documented, and useable sets of code. We will determine
this by the number of annotations we perform, as well as the difficulty in inserting those annotations such
that the checker runs without error. We are not attempting to demonstrate the soundness of the checker.

=========================

# Generating results

To automatically count the annotations we added to joda-time, checkout the AnnoFinal tag of [our fork of joda-time](https://github.com/mstaehely/joda-time), and run the script `count_annotations` that is in this repository from the root of the cloned joda-time repository. Our results are in `annotation_count.txt`.

To run the Index Checker on our fork, you should run `mvn compile` to download the joda-convert dependency, and then run
```
javac -classpath target/classes:$HOME/.m2/repository/org/joda/joda-convert/1.2/joda-convert-1.2.jar: -sourcepath src/main/java:target/generated-sources/annotations -d target/classes -processor index -implicit:class src/main/java/org/joda/time/*.java src/main/java/org/joda/time/*/*.java
```
to check the code. This may take some time.

To automatically time the compilation with and without the Index Checker, you need a recent copy of the Checker Framework, and you need to setup your `PATH` and `JAVA_HOME` environment as described in the building from source section of the checker framework manual.
Then you can run the `time_compile` command from this repository in the root directory of our fork. This will output how long it takes to compile both with and without the index checker. Our results are in `time_results.txt`.

