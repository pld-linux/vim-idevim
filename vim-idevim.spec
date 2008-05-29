Summary:	Control Gdb from inside Vim
Summary(pl.UTF-8):	Obsługa gdb z VIMa
Name:		vim-idevim
Version:	0.8
Release:	9
License:	GPL
Group:		Applications/Editors/Vim
#Source0:	http://vim.sourceforge.net/scripts/download.php?src_id=428
Source0:	idevim.tgz
# Source0-md5:	b63be71c432a7b67db75dde0afaaefc3
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-posix.patch
URL:		http://vim.sourceforge.net/scripts/script.php?script_id=168
Requires(post,postun):	/sbin/ldconfig
Requires(post,postun):	vim
# for _vimdatadir existence
Requires:	gdb
Requires:	vim-rt >= 4:6.3.058-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
This is plugin and library which turns Vim into the best Ide in the
world. :-) You can access all the Gdb functions and features; on
execution, the window is split, and the source position is shown in
the top window, while the data appears in the bottom.

%description -l pl.UTF-8
To jest wtyczka i biblioteka, które zmieniają VIMa w najlepszy IDE na
świecie. :-) Dają one dostęp do wszystkich funkcji Gdb. Podczas pracy
debuggera okno jest podzielone: aktualna linia kodu źródłowego
pokazana jest w górnym oknie, a dane są wyświetlane w dolnym.

%prep
%setup -qn gdbvim
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	LDBIN="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir} \
	VIMDIR=%{_vimdatadir} \
	VIM_VERSION="NONE"

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
umask 002
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%postun
/sbin/ldconfig
umask 002
echo ':helptags %{_vimdatadir}/doc' | vim -e -s

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so
%{_vimdatadir}/doc/*
%{_vimdatadir}/plugin/*
