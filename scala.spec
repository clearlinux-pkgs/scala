Name     : scala
Version  : 2.11.8
Release  : 1
URL      : https://github.com/scala/scala/archive/v2.11.8.tar.gz
Source0  : https://github.com/scala/scala/archive/v2.11.8.tar.gz
Source1  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/943cd5c8802b2a3a64a010efb86ec19bac142e40/lib/ant-contrib.jar
Source2  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/ddd7d5398733c4fbbb8355c049e258d47af636cf/lib/forkjoin.jar
Source3  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/3fc1e35ca8c991fc3488548f7a276bd9053c179d/lib/ant/ant-dotnet-1.0.jar
Source4  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/7b456ca6b93900f96e58cc8371f03d90a9c1c8d1/lib/ant/ant.jar
Source5  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/7e50e3e227d834695f1e0bf018a7326e06ee4c86/lib/ant/maven-ant-tasks-2.1.1.jar
Source6  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/2c61d6e9a912b3253194d5d6d3e1db7e2545ac4b/lib/ant/vizant.jar
Source7  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/981392dbd1f727b152cd1c908c5fce60ad9d07f7/test/files/lib/enums.jar
Source8  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/02fe2ed93766323a13f22c7a7e2ecdcd84259b6c/test/files/lib/annotations.jar
Source9  : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/b1ec8a095cec4902b3609d74d274c04365c59c04/test/files/lib/genericNest.jar
Source10 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/346d3dff4088839d6b4d163efa2892124039d216/test/files/lib/jsoup-1.3.1.jar
Source11 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/3794ec22d9b27f2b179bd34e9b46db771b934ec3/test/files/lib/macro210.jar
Source12 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/be8454d5e7751b063ade201c225dcedefd252775/test/files/lib/methvsfield.jar
Source13 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/cd33e0a0ea249eb42363a2f8ba531186345ff68c/test/files/lib/nest.jar
Source14 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/e737b123d31eede5594ceda07caafed1673ec472/test/files/codelib/code.jar
Source15 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/1b11ac773055c1e942c6b5eb4aabdf02292a7194/test/files/speclib/instrumented.jar
Source16 : https://dl.bintray.com/typesafe/scala-sha-bootstrap/org/scala-lang/bootstrap/a1883f4304d5aa65e1f6ee6aad5900c62dd81079/tools/push.jar
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear
BuildRequires : apache-ant
BuildRequires : curl
BuildRequires : git
BuildRequires : graphviz
BuildRequires : openjdk-dev
BuildRequires : scala-dep

%description
Scala Distribution
------------------
The Scala distribution requires Java 1.6 or above.

%prep
%setup -q -n scala-2.11.8
# Install libraries from scala repo
cp %{SOURCE1} lib/ant/
cp %{SOURCE2} lib/
cp %{SOURCE3} lib/ant/
cp %{SOURCE4} lib/ant/
cp %{SOURCE5} lib/ant/
cp %{SOURCE6} lib/ant/
cp %{SOURCE7} test/files/lib/
cp %{SOURCE8} test/files/lib/
cp %{SOURCE9} test/files/lib/
cp %{SOURCE10} test/files/lib/
cp %{SOURCE11} test/files/lib/
cp %{SOURCE12} test/files/lib/
cp %{SOURCE13} test/files/lib/
cp %{SOURCE14} test/files/codelib/
cp %{SOURCE15} test/files/speclib/
cp %{SOURCE16} tools/

%build
# Scala requires to be in a git repository in order to build successfully
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git init
git add *
git commit -m "a"

# Ant search for jar dependencies in {user.home}/.m2/repository.
export ANT_OPTS="-Duser.home=/usr/share/scala -Xms512M -Xmx2048M -Xss1M -XX:MaxPermSize=128M"
ant build docs
#ant docs

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/scala
pushd build/pack
cp -r bin/ lib/ %{buildroot}/usr/share/scala
#cp -r bin/ doc/ lib/ man/ %{buildroot}/usr/share/scala

# Remove unnecesary files
rm %{buildroot}/usr/share/scala/bin/*.bat

# Create symlinks for binaries
mkdir -p %{buildroot}/usr/bin
ln -s ../share/scala/bin/fsc %{buildroot}/usr/bin/fsc
ln -s ../share/scala/bin/scala %{buildroot}/usr/bin/scala
ln -s ../share/scala/bin/scalac %{buildroot}/usr/bin/scalac
ln -s ../share/scala/bin/scaladoc %{buildroot}/usr/bin/scaladoc
ln -s ../share/scala/bin/scalap %{buildroot}/usr/bin/scalap

%files
%defattr(-,root,root,-)
/usr/bin/fsc
/usr/bin/scala
/usr/bin/scalac
/usr/bin/scaladoc
/usr/bin/scalap
/usr/share/scala/bin/fsc
/usr/share/scala/bin/scala
/usr/share/scala/bin/scalac
/usr/share/scala/bin/scaladoc
/usr/share/scala/bin/scalap
/usr/share/scala/lib/jline.jar
/usr/share/scala/lib/scala-actors.jar
/usr/share/scala/lib/scala-compiler.jar
/usr/share/scala/lib/scala-continuations-library_2.11-1.0.2.jar
/usr/share/scala/lib/scala-continuations-plugin_2.11.7-1.0.2.jar
/usr/share/scala/lib/scala-library.jar
/usr/share/scala/lib/scala-parser-combinators_2.11-1.0.4.jar
/usr/share/scala/lib/scala-partest-extras.jar
/usr/share/scala/lib/scala-partest-javaagent.jar
/usr/share/scala/lib/scala-reflect.jar
/usr/share/scala/lib/scala-repl-jline-embedded.jar
/usr/share/scala/lib/scala-repl-jline.jar
/usr/share/scala/lib/scala-swing_2.11-1.0.2.jar
/usr/share/scala/lib/scala-xml_2.11-1.0.4.jar
/usr/share/scala/lib/scalap.jar
