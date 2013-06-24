Summary:	Resource Loading Framework
Name:		libloader
Version:	1.1.6
Release:	1
License:	LGPLv2+
Group:		Development/Java 
Url:		http://reporting.pentaho.org/
Source0:	http://downloads.sourceforge.net/jfreereport/%{name}-%{version}.zip
Patch0:		libloader-1.1.2-fix-build.patch
BuildArch:	noarch
BuildRequires:	ant
BuildRequires:	ant-contrib
BuildRequires:	ant-nodeps
BuildRequires:	java-devel
BuildRequires:	jpackage-utils
BuildRequires:	libbase >= 1.1.3
Requires:	java
Requires:	jpackage-utils
Requires:	libbase >= 1.1.3

%description
LibLoader is a general purpose resource loading framework. It has been
designed to allow to load resources from any physical location and to
allow the processing of that content data in a generic way 
BuildRequires:	totally transparent to the user of that library.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Development/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

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
%doc licence-LGPL.txt README.txt ChangeLog.txt
%{_javadir}/%{name}-%{version}.jar
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

