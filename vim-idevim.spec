Summary:	Control Gdb from inside Vim
Summary(pl):	Obs³uga gdb z VIMa
Name:		vim-idevim
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Editors/Vim
#Source0:	http://vim.sourceforge.net/scripts/download.php?src_id=428
Source0:	idevim.tgz
Patch0:		%{name}-Makefile.patch
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=168
BuildRequires:	vim >= 6.0
BuildConflicts:	vim >= 6.1
Requires:	vim >= 6.0
Conflicts:	vim >= 6.1
Requires:	gdb
Requires(postun):	vim >= 6.0
Requires(post):	vim >= 6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vim60

%description
This is plugin and library which turns Vim into the best Ide in the
world. :-) You can access all the Gdb functions and features; on
execution, the window is split, and the source position is shown in
the top window, while the data appears in the bottom.

%description -l pl
To jest wtyczka i biblioteka, które zmieniaj± VIMa w najlepszy IDE na
¶wiecie. :-) Daj± one dostêp do wszystkuch funkcji Gdb. Podczas pracy
debuggera okno jest podzielone: aktualna linia kodu ¼ród³oweo pokazana
jest w górnym oknie, a dane s± wy¶wietlane w dolnym.

%prep
%setup -qn gdbvim
%patch0 -p1

%build
%{__make} CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre -p /sbin/ldconfig

%post
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%postun
/sbin/ldconfig
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*
