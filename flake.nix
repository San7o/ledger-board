{
  description = "Python venv development template";

  inputs = {
    utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    utils,
    ...
  }:
    utils.lib.eachDefaultSystem (system: let
      pkgs = import nixpkgs {inherit system;};
      pythonPackages = pkgs.python3Packages;
    in {
      devShells.default = pkgs.mkShell {
        name = "python-venv";
        venvDir = "backend/.venv";
        buildInputs = [

          # Kubernetes dependencies
          pkgs.kind      # tool to manage k8s resources
          pkgs.kompose   # convert docker-compose to k8s
          pkgs.kubectl   # k8s command line tool


          # Database dependencies
          pkgs.redis

          # Frontend dependencies
          pkgs.nodejs_20


          # Backend dependencies
          # A Python interpreter including the
          # 'venv' module is required to bootstrap
          # the environment.
          pythonPackages.python

          # This executes some shell code to initialize
          # a venv in $venvDir before
          # dropping into the shell
          pythonPackages.venvShellHook

          # Those are dependencies that we would
          # like to use from nixpkgs, which will
          # add them to PYTHONPATH and thus make
          #them accessible from within the venv.
          # pythonPackages.numpy


          # kafka dependencies
          pkgs.kafkactl    # interact with kafka

          # General Development tools
          pkgs.act         # github actions simulator
          pkgs.tig         # git commit viewer
          pkgs.cmake       # build system


          # C libraries needed for some python packages
          pkgs.zlib
          pkgs.libGL
          pkgs.glib

        ];

        # Run this command, only after creating the
        # virtual environment
        postVenvCreation = ''
          unset SOURCE_DATE_EPOCH
          pip install -r backend/requirements.txt
        '';


        LD_LIBRARY_PATH = "${pkgs.zlib}/lib:${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.libGL}/lib:${pkgs.glib.out}/lib";

        # Now we can execute any commands within
        # the virtual environment.
        # This is optional and can be left out to
        # run pip manually.
        postShellHook = ''
          # allow pip to install wheels
          unset SOURCE_DATE_EPOCH
        '';
      };
    });
}
