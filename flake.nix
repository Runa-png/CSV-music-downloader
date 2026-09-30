{
  description = "RunaCipher";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
        };

        python = pkgs.python313;
      in {
        devShells.default = pkgs.mkShell {
          packages = [
            python
            pkgs.python313Packages.pandas
            pkgs.python313Packages.yt-dlp
            pkgs.python313Packages.fuzzywuzzy
          ];
        };
      });
}
