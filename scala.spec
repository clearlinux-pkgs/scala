Name     : scala
Version  : 2.12.4
Release  : 9
URL      : http://localhost/cgit/projects/scala/snapshot/scala-2.12.4.tar.gz
Source0  : http://localhost/cgit/projects/scala/snapshot/scala-2.12.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause-Clear MIT Apache-2.0 BSD-2-Clause

%description
Scala Distribution
------------------
The Scala distribution requires Java 1.6 or above.

%prep
%setup -q -n scala-2.12.4

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/scala
#cp -r man/ %{buildroot}/usr/share/
cp -r bin/ doc/ lib/ %{buildroot}/usr/share/scala/

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
/usr/share/scala/doc/licenses/mit_jquery.txt
/usr/share/scala/doc/licenses/mit_sizzle.txt
/usr/share/scala/doc/licenses/mit_tools.tooltip.txt
/usr/share/scala/lib/jline.jar
/usr/share/scala/lib/scala-compiler-doc.jar
/usr/share/scala/lib/scala-compiler.jar
/usr/share/scala/lib/scala-library.jar
/usr/share/scala/lib/scala-reflect.jar
/usr/share/scala/lib/scala-repl-jline-embedded.jar
/usr/share/scala/lib/scala-repl-jline.jar
/usr/share/scala/lib/scala-swing_2.12-2.0.0.jar
/usr/share/scala/lib/scala-xml_2.12-1.0.6.jar
/usr/share/scala/lib/scalap.jar
