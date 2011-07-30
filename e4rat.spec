Summary:	A toolset to accelerate the boot process as well as application startups
Name:		e4rat
Version:	0.2.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/project/%{name}/%{version}/%{name}_%{version}_src.tar.gz
# Source0-md5:	cbb1f3cdd2b8c96b4402028da07b11f2
URL:		http://e4rat.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
e4rat ("Ext4 - Reducing Access Times") is a toolset to accelerate the
boot process as well as application startups. Through physical file
realloction e4rat eliminates both seek times and rotational delays.
This leads to a high disk transfer rate. Placing files on disk in a
sequentially ordered way allows to efficiently read-ahead files in
parallel to the program startup. The combination of sequentially
reading and a high cache hit rate may reduce the boot time by a factor
of three, as the example below shows.

e4rat is based on the online defragmentation ioctl EXT4_IOC_MOVE_EXT
from the Ext4 filesystem, which was introduced in Linux Kernel 2.6.31.
Other filesystem types and/or earlier versions of extended filesystems
are not supported.

%prep
%setup -q

%build
cmake .

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/*
