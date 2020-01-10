Name:           maven-shared-jar
Version:        1.1
Release:        8%{?dist}
# Maven-shared defines maven-shared-jar version as 1.1
Epoch:          1
Summary:        Maven JAR Utilities
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-shared-jar
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{name}/%{version}/%{name}-%{version}-source-release.zip

BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.apache.bcel:bcel)
BuildRequires:  mvn(org.apache.maven:maven-model)
BuildRequires:  mvn(commons-collections:commons-collections)
BuildRequires:  mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires:  mvn(org.apache.maven:maven-artifact)
BuildRequires:  mvn(org.codehaus.plexus:plexus-digest)

Obsoletes:      maven-shared-jar < %{epoch}:%{version}-%{release} 
Provides:       maven-shared-jar = %{epoch}:%{version}-%{release}

%description
Utilities that help identify the contents of a JAR, including Java class
analysis and Maven metadata analysis.

This is a replacement package for maven-shared-jar

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}
    
%description javadoc
API documentation for %{name}.


%prep
%setup -q

%pom_add_dep org.codehaus.plexus:plexus-container-default

find -type f -iname '*.jar' -delete

# Replace plexus-maven-plugin with plexus-component-metadata
find -name 'pom.xml' -exec sed \
    -i 's/<artifactId>plexus-maven-plugin<\/artifactId>/<artifactId>plexus-component-metadata<\/artifactId>/' '{}' ';'
find -name 'pom.xml' -exec sed \
    -i 's/<goal>descriptor<\/goal>/<goal>generate-metadata<\/goal>/' '{}' ';'

%mvn_file : %{name}

%build
# Tests require the jars that were removed
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Fri Aug  1 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-8
- Add missing build-requires on maven-shared
- Resolves: rhbz#1074931

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:1.1-7
- Mass rebuild 2013-12-27

* Thu Sep 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-6
- Fix BuildRequires

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 1:1.1-5
- Migrate away from mvn-rpmbuild (Resolves: #997500)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:1.1-4
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 23 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-2
- Removed jars and skipped tests

* Tue Jan 15 2013 Tomas Radej <tradej@redhat.com> - 1:1.1-1
- Initial version

