using JSON
using Peaks
using OrderedCollections
using DataFrames
using LaTeXStrings
using StatsBase
using MultivariateStats
using SharedArrays
using Clustering
using CSV
using Distances
using Distributed
using JLD2


function build_grid_return_vals(data)
	vals = map(x -> x, data |> values)
	long_vectores = @. vals |> first  |> size |> first
	max_long = maximum(long_vectores)
	idx_maxlong = findall( x -> (size(x[1])[1]) == max_long, vals ) |> first
	first(vals[idx_maxlong]), vals
end

function distributed_build_interpolated_data(grilla, vals) 
	@info "Running long function"
	V = SharedArray{Float16}(size(vals)[1], size(grilla)[1])
	n = 1
	@distributed for (x,y) in vals
		y_int = zeros(Float32, size(grilla))
		idxs = map(eachcol(abs.(grilla .- x'))) do col
			argmin(col)
		end
		y_int[idxs] = y
		V[n,:] = y_int
		n += 1
		n % 100 == 0 && @info "Iteracion $n"
	end
	V
end


const master_df = CSV.File("2019-07-01-FSR-public_7061.csv") |> DataFrame
const patterns = JSON.parsefile("./patterns_540.json",
				dicttype = Dict,
				inttype = Int64
				)
const tgt_pattern = CSV.File("xe.dat") |> DataFrame


data = patterns 
data["target.cif"] = tgt_pattern.theta, tgt_pattern.int
grid, vals = build_grid_return_vals(data)
vals = vals[begin:20]
MatrizEspectros = distributed_build_interpolated_data(grid, vals )
save("output/espectros.jld2", Dict(:datos_espectros_interpolados => MatrizEspectros) )