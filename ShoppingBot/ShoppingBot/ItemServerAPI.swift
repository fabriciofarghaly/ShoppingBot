//
//  ItemServerAPI.swift
//  ShoppingBot
//
//  Created by Charlie Mulholland on 11/28/22.
//

import Foundation


struct ItemServerAPI {
    // MARK: Change IP_Address to the IP address of the computer running the web server
    private static let baseURLString = "http://<#T##IP_Address#>:8080"
    
    static let session: URLSession = {
        let sess = URLSession(configuration: .default)
        return sess
    }()
    
    static func getBudget(completion: @escaping(Dictionary<String,Any>?) -> Void) {
        let components = URLComponents(string: "\(baseURLString)/budget")!
                
        var request = URLRequest(url: components.url!)
        request.httpMethod = "GET"
        let task = session.dataTask(with: request) {
            (data, response, error) -> Void in
                    
            guard let downloaded = data else {
                print("Nothing downloaded")
                OperationQueue.main.addOperation {
                    completion(nil)
                }
                return
            }
            let jsonObject = processJsonData(from: downloaded)
            OperationQueue.main.addOperation {
                completion(jsonObject)
            }
        }
        task.resume()
    }
    
    static func setBudget(new_budget: String, completion: @escaping(Dictionary<String, Any>?) -> Void) {
        var components = URLComponents(string: "\(baseURLString)/budget")!
        
        components.queryItems = [
            URLQueryItem(name: "new_budget", value: new_budget)
        ]
        
                
        var request = URLRequest(url: components.url!)
        request.httpMethod = "POST"
        let task = session.dataTask(with: request) {
            (data, response, error) -> Void in
                    
            guard let downloaded = data else {
                print("Nothing downloaded")
                OperationQueue.main.addOperation {
                    completion(nil)
                }
                return
            }
            let jsonObject = processJsonData(from: downloaded)
            OperationQueue.main.addOperation {
                completion(jsonObject)
            }
        }
        task.resume()
    }
    
    static func removeLastItem() {
        var components = URLComponents(string: "\(baseURLString)/remove_item")!
        
        var request = URLRequest(url: components.url!)
        request.httpMethod = "POST"
        let task = session.dataTask(with: request) {
            (data, response, error) -> Void in
                    
            guard let downloaded = data else {
                print("Nothing downloaded")
                return
            }
            print(downloaded)
            return
        }
        task.resume()
        
    }
    
    static func processJsonData(from data: Data) -> Dictionary<String,Any>? {
        do {
            let jsonObj = try JSONSerialization.jsonObject(with: data) as! Dictionary<String,Any>
            return jsonObj
        } catch {
            print(error)
            return nil
        }
    }
}
