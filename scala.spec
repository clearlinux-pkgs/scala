Name     : scala
Version  : 2.11.8
Release  : 1
URL      : http://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz
Source0  : http://downloads.lightbend.com/scala/2.11.8/scala-2.11.8.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear

%description
Scala Distribution
------------------
The Scala distribution requires Java 1.6 or above.

%prep
%setup -q -n scala-2.11.8

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/scala
cp -r bin/ doc/ lib/ man/ %{buildroot}/usr/share/scala

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
/usr/share/scala/doc/LICENSE.md
/usr/share/scala/doc/License.rtf
/usr/share/scala/doc/README
/usr/share/scala/doc/licenses/apache_jansi.txt
/usr/share/scala/doc/licenses/bsd_asm.txt
/usr/share/scala/doc/licenses/bsd_jline.txt
/usr/share/scala/doc/licenses/mit_jquery-layout.txt
/usr/share/scala/doc/licenses/mit_jquery-ui.txt
/usr/share/scala/doc/licenses/mit_jquery.txt
/usr/share/scala/doc/licenses/mit_sizzle.txt
/usr/share/scala/doc/licenses/mit_tools.tooltip.txt
/usr/share/scala/doc/tools/css/style.css
/usr/share/scala/doc/tools/fsc.html
/usr/share/scala/doc/tools/images/external.gif
/usr/share/scala/doc/tools/images/scala_logo.png
/usr/share/scala/doc/tools/index.html
/usr/share/scala/doc/tools/scala.html
/usr/share/scala/doc/tools/scalac.html
/usr/share/scala/doc/tools/scaladoc.html
/usr/share/scala/doc/tools/scalap.html
/usr/share/scala/lib/akka-actor_2.11-2.3.10.jar
/usr/share/scala/lib/config-1.2.1.jar
/usr/share/scala/lib/jline-2.12.1.jar
/usr/share/scala/lib/scala-actors-2.11.0.jar
/usr/share/scala/lib/scala-actors-migration_2.11-1.1.0.jar
/usr/share/scala/lib/scala-compiler.jar
/usr/share/scala/lib/scala-continuations-library_2.11-1.0.2.jar
/usr/share/scala/lib/scala-continuations-plugin_2.11.8-1.0.2.jar
/usr/share/scala/lib/scala-library.jar
/usr/share/scala/lib/scala-parser-combinators_2.11-1.0.4.jar
/usr/share/scala/lib/scala-reflect.jar
/usr/share/scala/lib/scala-swing_2.11-1.0.2.jar
/usr/share/scala/lib/scala-xml_2.11-1.0.4.jar
/usr/share/scala/lib/scalap-2.11.8.jar
/usr/share/scala/man/man1/fsc.1
/usr/share/scala/man/man1/scala.1
/usr/share/scala/man/man1/scalac.1
/usr/share/scala/man/man1/scaladoc.1
/usr/share/scala/man/man1/scalap.1
