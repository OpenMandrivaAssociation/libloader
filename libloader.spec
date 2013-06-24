Name:           libloader
Version:        1.1.6
Release:        %mkrel 3
Summary:        Resource Loading Framework
License:        LGPLv2+
Group:          Development/Java 
Source0:        http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
URL:            http://reporting.pentaho.org/
BuildRequires:  ant, ant-contrib, ant-nodeps, java-devel, jpackage-utils
BuildRequires:  libbase >= 1.1.3
Requires:       java, jpackage-utils, libbase >= 1.1.3
BuildArch:      noarch
Patch0:         libloader-1.1.2-fix-build.patch

%description
LibLoader is a general purpose resource loading framework. It has been
designed to allow to load resources from any physical location and to
allow the processing of that content data in a generic way, totally
transparent to the user of that library.


%package javadoc
Summary:        Javadoc for %{name}
Group:          Documentation
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
Javadoc for %{name}.


%prep
%setup -q -c
%patch0 -p0
find . -name "*.jar" -exec rm -f {} \;
mkdir -p lib
build-jar-repository -s -p lib libbase commons-logging-api
cd lib
ln -s %{_javadir}/ant ant-contrib

%build
ant jar javadoc
for file in README.txt licence-LGPL.txt ChangeLog.txt; do
    tr -d '\r' < $file > $file.new
    mv $file.new $file
done

%install
mkdir -p %{buildroot}%{_javadir}
cp -p ./dist/%{name}-%{version}.jar %{buildroot}%{_javadir}
pushd %{buildroot}%{_javadir}
ln -s %{name}-%{version}.jar %{name}.jar
popd

mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp bin/javadoc/docs/api %{buildroot}%{_javadocdir}/%{name}

%files
%defattr(0644,root,root,0755)
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%defattr(0644,root,root,0755)
%{_javadocdir}/%{name}


%changelog

* Sat Jan 12 2013 umeabot <umeabot> 1.1.6-3.mga3
+ Revision: 357681
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Oct 14 2012 ennael <ennael> 1.1.6-2.mga3
+ Revision: 305447
- Documentation group

* Sat Jan 21 2012 kamil <kamil> 1.1.6-1.mga2
+ Revision: 198955
- new version 1.1.6
- drop gcj support
- rediff and rename patch to fix-build.patch
- clean .spec

* Fri Mar 18 2011 dmorgan <dmorgan> 1.1.3-2.mga1
+ Revision: 74331
- Really build without gcj

* Mon Jan 24 2011 dmorgan <dmorgan> 1.1.3-1.mga1
+ Revision: 35928
- Adapt for mageia
- imported package libloader

